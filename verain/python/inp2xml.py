from __future__ import absolute_import, division, print_function

import pyparsing as pp
import os, argparse
# import Utils.flatten

from Templates.CASEID import CASEID
from Templates.STATE import STATE
from Templates.CORE import CORE
from Templates.EDITS import EDITS
from Templates.ASSEMBLIES import ASSEMBLY
from Templates.INSERTS import INSERT
from Templates.CONTROLS import CONTROL
from Templates.DETECTORS import DETECTOR
from Templates.SHIFT import SHIFT
from Templates.MPACT import MPACT
from Templates.COBRATF import COBRATF
from Templates.INSILICO import INSILICO

scriptDir = os.path.dirname(os.path.abspath(__file__))

def convertNum(tokens):
    val = tokens[0]
    try:
        return int( val )
    except:
        return float( val )

class VeraInConverter(object):
    sectionNames = {
        "CASEID": CASEID,
        "STATE": STATE,
        "CORE": CORE,
        "ASSEMBLY": ASSEMBLY,
        "CONTROL": CONTROL,
        "DETECTOR": DETECTOR,
        "INSERT": INSERT,
        "EDITS": EDITS,
        "COUPLING": CASEID,
        # Simulator code config blocks
        "SHIFT": SHIFT,
        "COBRATF": COBRATF,
        "INSILICO": INSILICO,
        "MPACT": MPACT,
        "BISON": CASEID,
        "MAMBA1D": CASEID,
        "TIAMAT": CASEID
    }

    cellSectionNames = ["ASSEMBLY", "CONTROL", "DETECTOR", "INSERT"]
    keywordSpace = 2
    inpbnf = None
    includebnf = None

    def __init__(self):
        # keep things neat - track # of spaces indented as lists are added/closed
        self.indent = 0
        # list of strings to output - one per line
        self.outList = []
        # pieces of the parsed input we need to keep track of
        self.caseID = None
        self.core = None
        self.states = []
        self.cellSections = {}
        self.sections = []
        self.keyWordDef = None

    # when a section is parsed, stick it in the appropriate list/place
    def handleSection(self, toks):
        section = toks[0]
        sectionName = section[0]
        if sectionName == "CASEID":
            self.caseID = section
        elif sectionName == "CORE":
            self.core = section
        elif sectionName == "STATE":
            self.states.append(section)
        elif sectionName in VeraInConverter.cellSectionNames:
            # each of these has maps and sub-sections, and may appear more than once. Group them.
            if not sectionName in self.cellSections:
                self.cellSections[sectionName] = []
            self.cellSections[sectionName].append(section)
        else:
            self.sections.append(section)
            # Possibly pre-process the tokens so we can extract global info, like maps.

    def handleSectionName(self, toks):
        sectionName = toks[0]
        # Set keywords that this section can parse. Must be set before values are parsed.
        if self.keyWordDef:
            paramDict = VeraInConverter.sectionNames[sectionName]
            self.keyWordDef << pp.oneOf(paramDict["_content"].keys())
            # print("DBG keywords", self.keyWordDef.expr)

    def replaceWithFile(self, toks):
        # given a filename, replace with its contents
        filename = toks[1]
        incData = ""
        try:
            incFile = open(os.path.join(scriptDir, "../scripts/Init", filename), "r")
            incData = "  " + "  ".join( incFile.readlines() )
        except:
            raise ValueError("Unable to open included file, '%s'" % filename)

        return incData

    def addDefaults(self, toks):
        # print("Got section:", toks[0], toks[1])
        sectionLine = "[%s] %s" % (toks[0], toks[1])

        filename = "%s.ini" % toks[0]
        incData = ""
        try:
            incFile = open(os.path.join(scriptDir, "../scripts/Init", filename), "r")
            incData = "  " + "  ".join( incFile.readlines() )
            # print("Added defaults, section:", toks[0])
        except:
            pass
        if incData:
            return sectionLine + incData
        return sectionLine

    def inpfile_BNF(self):
        if not VeraInConverter.inpbnf:
            # allow us to detect separate lines, but still ignore space between words
            pp.ParserElement.setDefaultWhitespaceChars(' \t')

            # punctuation
            lbrack = pp.Literal("[").suppress()
            rbrack = pp.Literal("]").suppress()
            # equals = pp.Literal("=").suppress()
            semi   = pp.Literal(";").suppress()
            EOL = pp.LineEnd().suppress()
            nonsemi = "".join( [ c for c in pp.printables if c != ";" ] )

              # ignore comments completely
            comment = pp.Literal("!") + pp.Optional( pp.restOfLine )

            # numbers
            point = pp.Literal( "." )
            e     = pp.CaselessLiteral( "E" )
            plusorminus = pp.Literal('+') | pp.Literal('-')
            number = pp.Word(pp.nums)
            integer = pp.Combine( pp.Optional(plusorminus) + number )
            floatnumber = pp.Combine( integer +
                                   pp.Optional( point + pp.Optional(number) ) +
                                   pp.Optional( e + integer )
                                 ).setParseAction(convertNum)

            # we don't want to keep the quotes around a quoted title or name
            quoteStr = pp.quotedString.addParseAction(pp.removeQuotes)
            # maps accept a shortcut, size*val
            mapProductDef = number.setParseAction(convertNum) + pp.Literal("*") + pp.Word(nonsemi)

            # keywords start an input card, two+ space indent.
            # Acceptible keywords defined by the section we are in, filled by handleSectionName()
            self.keyWordDef = pp.Forward()  # allowed: pp.Word( pp.alphas, pp.alphanums + "_" )
            keyWordWhite = pp.White(" ", min=VeraInConverter.keywordSpace).suppress()
            spaceKeyWordDef = keyWordWhite + self.keyWordDef

            # values, value lists, or indented value lists complete the card
            # can't exclude keywords here, 'boron' is both a keyword and value.
            # also use '^', to make sure we get the longest match, for tags like '80IFBA'
            valueDef = (quoteStr | mapProductDef | pp.ZeroOrMore( floatnumber ^ pp.Word(nonsemi) ))
            valueDefEOL = valueDef + pp.OneOrMore(EOL)
            valueDefSemi = valueDef + semi
            # values must be indented more than the keywords, and not be a keyword.
            valueWhite = pp.White(" ", min=(VeraInConverter.keywordSpace+1)).suppress()
            indentedValueDef = valueWhite + ~self.keyWordDef + valueDefEOL

            singleCardDef = pp.Group( spaceKeyWordDef + pp.Group(valueDefEOL + pp.Optional( pp.OneOrMore(pp.Group(indentedValueDef))) ) )
            # special handling for semi-separated-list of cards on one line for [STATE] blocks
            inlineCardDefSemi = pp.Group( self.keyWordDef + pp.Group(valueDefSemi) )
            inlineCardDefEOL = pp.Group( self.keyWordDef + pp.Group(valueDefEOL) )

            # section header complicated by possible inline cards on the same line.
            sectionNamePlain = pp.oneOf( VeraInConverter.sectionNames.keys() )
            sectionNameDef = sectionNamePlain.setParseAction(self.handleSectionName)
            sectionHeader = lbrack + sectionNameDef + rbrack + \
                ( (pp.ZeroOrMore(inlineCardDefSemi | semi) + inlineCardDefEOL) | pp.ZeroOrMore(EOL) )

            # card def is complicated by possible inline cards on the same line
            cardDef = singleCardDef | (pp.OneOrMore(inlineCardDefSemi | semi) + inlineCardDefEOL)

            # using pp.Dict would allow retrieval of named data fields as attributes of the parsed results
            # this is a problem with [STATE] and cell-map blocks, which can occur more than once.
            sectionDef = pp.Group( sectionHeader + pp.ZeroOrMore( cardDef ) | EOL).setParseAction(
                self.handleSection
            )
            VeraInConverter.inpbnf = pp.OneOrMore( sectionDef )

            VeraInConverter.inpbnf.ignore( comment )

            #
            # additional parser to include files in this file, using some of our rules
            VeraInConverter.includebnf = (keyWordWhite + "include" + \
              (quoteStr | pp.Word(nonsemi))).setParseAction(self.replaceWithFile) | \
              (lbrack + sectionNamePlain + rbrack + (pp.lineEnd | pp.Combine(pp.restOfLine + pp.lineEnd))).setParseAction(self.addDefaults)
            VeraInConverter.includebnf.ignore( comment )

        return VeraInConverter.inpbnf

    def include_BNF(self):
        if not VeraInConverter.inpbnf:
            self.inpfile_BNF()
        return VeraInConverter.includebnf

    # verify that this card's contents are as expected.
    # data types, length, format, etc.
    def verifyCard(self, card, spec):
        # call methods specified that verify this card's content
        for checkItem in spec["_check"]:
            if type(checkItem) == list:
                # first item is method to call, the rest are args.
                checkItem[0](card[1], *checkItem[1:])
            else:
                checkItem(card[1])

    # extract cards that trigger a section ParameterList in the output.
    def extractSectionParams(self, cards, paramDict):
        sectionParams = []
        for card in cards:
            paramName = card[0]
            # _sectionParams is a card-name list, like ["axial"]
            if paramName in paramDict["_sectionParams"]:
                sectionParams.append(card)
        return sectionParams

    # some cards need info from a different card - like a map needs a size.
    # extract those cards that referenced by another card
    def extractRefParams(self, cards, paramDict):
        if "refs" in paramDict:  # or not "_refParams" in paramDict:
            # already done, or nothing to do
            return False
        refList = paramDict["_refParams"] if "_refParams" in paramDict else []
        refParams = {}
        for card in cards:
            paramName = card[0]
            # _refParams is a card-name list, like ["npins", "foo"]
            if paramName in refList:
                refParams[str(card[0])] = card[1]
            # Second kind of ref - _output may have _refParam, handled
            # during outputSingleCard
        paramDict["_refs"] = refParams
        return True

    def removeRefParams(self, paramDict):
        if "refs" in paramDict:
            del paramDict["_refs"]

    # A card says it wants to use a different card's value by including a "ref:foo:index" or "ref:foo_array" arg
    # in it's output _value list.
    def replaceRefArgs(self, argList, refs):
        for i, arg in enumerate(argList):
            if type(arg) == str and arg[0:4] == "ref:":
                argSplit = arg.split(":")
                key = argSplit[1]
                # import ipdb; ipdb.set_trace()
                # print("replaceRefArgs", key, refs)
                # taking the indicated value of the card there's a second colon, else get whole array for maps.
                if key in refs:
                    argList[i] = refs[key][int(argSplit[2])] if len(argSplit) == 3 else refs[key]
                else:
                    raise ValueError("Replacement arg '%s' not available" % key)

    def outputParam(self, name, ptype, value, optional=False):
        # TODO this works for empty strings and integers > 0, but what about 0?
        if optional and value == None:
            return
        elif type(value) == str and value == "":
            raise ValueError("Non-optional parameter '%s' with empty value" % name)
        self.outList.append('%s<Parameter name="%s" type="%s" value="%s"/>' % (
            " " * self.indent, name, ptype, value) )

    def addOuputRef(self, card, outSpec, outName, refs):
        # see if we should add to refs for this output
        if refs and "_refParam" in outSpec:
            genRefList = outSpec["_refParam"]
            # add ref under the output name, not the card name.
            newRef = genRefList[0](card[1], *genRefList[1:])
            if not outName in refs:
                refs[outName] = newRef
            elif type(refs[outName]) is set:
                refs[outName] |= newRef
            else:
                print("Unhandled combination, replacing ", refs[outName])
                refs[outName] = newRef

            # print("DBG GENREF", outName, refs[str(outName)])

    def outputSingleCard(self, card, spec, paramName, refs=None):
        for outSpec in spec["_output"]:
            # "_name" is an override for the input paramName
            outName = outSpec["_name"] if "_name" in outSpec else paramName
            # output type is modified for arrays
            if "_type" in outSpec:
                outType = outSpec["_type"] if outSpec["_pltype"] != "array" else "Array(%s)" % outSpec["_type"]
            else:
                outType = "none"
            # allow optional output, if array can have values tacked on the end.
            optionalFlag = "_optional" in outSpec and outSpec["_optional"]
            if outSpec["_pltype"] == "parameter" or outSpec["_pltype"] == "array":
                if type(outSpec["_value"]) == list:
                    # make a copy
                    genValueList = outSpec["_value"][:]
                    # see if there are any args that need to be replaced with "_refs"
                    if refs:
                        self.replaceRefArgs(genValueList, refs)

                    # first item is method to call, the rest are args.
                    self.outputParam( outName, outType, genValueList[0](card[1], *genValueList[1:]), optionalFlag)
                else:
                    # the only item is a method to call, like copy_value
                    self.outputParam( outName, outType, outSpec["_value"](card[1]), optionalFlag)
                # add refs
                self.addOuputRef(card, outSpec, outName, refs)
            else:
                # this shouldn't get hit, because we've already handled lists
                raise ValueError("Unexpected parameter type, '%s', for '%s'" % (outSpec["_pltype"], outName))

    # Should we output this card? Does it have a "_condition" that needs to be true?
    def shouldOutputCard(self, card, spec, paramDict, refs):
        if "_condition" in spec:
            # set up a utility method which decides about this card.
            conditionList = spec["_condition"][:]
            # there should be args that need to be replaced with "_refs"
            if refs:
                self.replaceRefArgs(conditionList, refs)
            return conditionList[0](card[1], *conditionList[1:])

        return True

    # Output a list, with the inner params from one or more cards, extracted and grouped.
    def outputCardList(self, listCards, listName, paramDict, refs):
        # outer list, examples in MPACT or SHIFT
        self.outputListStart(listName)
        # these cards were extracted into a dict, so we don't want to extract again, this time we output normally.
        self.outputCards(listCards, paramDict, useDict=False)
        self.outputListEnd(listName)

    # Output a list of lists, with the inner lists derived from a single input card.
    def outputCardListOfLists(self, listCards, paramDict, refs):
        paramName = listCards[0][0]
        if paramName in paramDict["_content"]:
            spec = paramDict["_content"][paramName]
            # outer list, like ASSEMBLIES or CONTROLS
            self.outputListStart(spec["_name"])
            for card in listCards:
                listKey = card[1][0]
                listName = spec["_listName"] % str(listKey)
                if self.shouldOutputCard(card, spec, paramDict, refs):
                    self.outputListStart(listName)
                    self.outputSingleCard(card, spec, paramName, refs)
                    self.outputListEnd(listName)

            self.outputListEnd(spec["_name"])

    # output a list of cards.
    # Cards whose type is "parameter" or "array" are unique
    # Earlier values are replaced by later values - allows for inclusion of defaults
    # Lists are collected together, and output together
    # a section card (like 'axial') causes other section cards to be ignored.
    def outputCards(self, cards, paramDict, useDict=True):
        # Collect cards that appear more than once, to be output together
        listCards = {}
        # collect cards that are unique, but should be output inside a list
        groupedCards = {}
        # all other unique cards, custom values over-write defaults
        cardDict = {}
        # listParamName = ""
        sectionName = ""
        refs = paramDict["_refs"] if "_refs" in paramDict else None
        # if there is a section card avail, make sure other section cards aren't output.
        if "_section" in paramDict:
            sectionKey = paramDict["_section"][1][0]
            sectionName = paramDict["_section"][0]
        for card in cards:
            paramName = card[0]
            if paramName in paramDict["_content"]:
                spec = paramDict["_content"][paramName]
                # verify the conents of the card, first
                if "_check" in spec:
                    self.verifyCard(card, spec)
                # lists - see if any existing cardlist has terminated and needs to be output.
                # if listCards and (not ("_pltype" in spec and spec["_pltype"] == "list") or listParamName != paramName):
                #     # handle the saved list of cards as a list.
                #     self.outputCardListOfLists(listCards, paramDict, refs)
                #     # reset the cardList
                #     listCards = []
                #     listParamName = ""

                # lists - gather cards first.
                # TODO embedded list, "graph" in "parallel_env"
                if useDict and "_inlist" in spec:
                    # gather separate cards into a list
                    dictKey = spec["_inlist"]
                    if not dictKey in groupedCards:
                        groupedCards[dictKey] = []
                    groupedCards[dictKey].append(card)
                    # once case ("Np") needs to duplicate output, not in list, too.
                    if "_notInList" in spec["_output"][0] and spec["_output"][0]["_notInList"]:
                        cardDict[paramName] = (card, spec, paramName)
                # single card type gathered, outputing list-of-list
                elif "_pltype" in spec and spec["_pltype"] == "list":
                    if not paramName in listCards:
                        listCards[paramName] = []
                    listCards[paramName].append(card)
                # keep if it's not a section card, or if it is a section card, and the key matches.
                elif paramName != sectionName or card[1][0] == sectionKey:
                    # over-write earlier entries with later entries
                    cardDict[paramName] = (card, spec, paramName)
            else:
                # this shouldn't get hit, because of keyword lists for sections.
                raise ValueError("Unexpected card name, '%s', with tag '%s'" % (paramName, card[1][0]))

        # output single cards, sorting is futile, since this isn't the output name.
        for dictKey in sorted(cardDict.keys()):
            card, spec, paramName = cardDict[dictKey]
            self.outputSingleCard(card, spec, paramName, refs)
        # output any list-of-lists.
        for dictKey in listCards:
            self.outputCardListOfLists(listCards[dictKey], paramDict, refs)
        # output any cards grouped into lists
        for dictKey in groupedCards:
            self.outputCardList(groupedCards[dictKey], dictKey, paramDict, refs)


    # Start and end a list, sets indent for contents.
    def outputListStart(self, name):
        self.outList.append('%s<ParameterList name="%s">' % (" " * self.indent, name))
        self.indent += 2
    def outputListEnd(self, name=None):
        self.indent -= 2
        self.outList.append('%s</ParameterList>' % (" " * self.indent))

    def outputSection(self, section, inSectionName=None):
        sectionName = inSectionName if inSectionName else section[0]

        paramDict = VeraInConverter.sectionNames[section[0]]
        ordered = paramDict["_order"] if "_order" in paramDict else None
        # if we are called outside outputCellSection (like for CORE), add our own refs
        addedRefs = self.extractRefParams(section, paramDict)
        cardList = section[1:]
        # import ipdb; ipdb.set_trace()
        self.outputListStart(sectionName)

        if ordered:
            orderedCards = []
            for key in ordered:
                orderedCards.extend([card for card in cardList if card[0] == key])
            cardList = [card for card in cardList if card[0] not in ordered]
            self.outputCards(orderedCards, paramDict)

        self.outputCards(cardList, paramDict)

        self.outputListEnd(sectionName)
        if addedRefs:
            self.removeRefParams(paramDict)

    def outputCellSection(self, sectionList):
        # one or more sections that define assemblies, inserts, etc.
        # Outer group list, but each section may output several groups
        # when it hits the 'axial' cards.
        sectionName = sectionList[0][0]
        paramDict = VeraInConverter.sectionNames[sectionName]
        groupName = paramDict["_groupName"]

        self.outputListStart(groupName)
        # iterate over [GROUP] tags in input
        for outerSection in sectionList:
            # First, extract cards (like 'axial') which can trigger a section
            sectionParams = self.extractSectionParams(outerSection, paramDict)
            # this cardlist includes all the 'axial' cards, need to mark one current
            cardList = outerSection[1:]
            # now loop over output groups
            for sectionCard in sectionParams:
                # add the current sectionParam to the dict
                paramDict["_section"] = sectionCard
                sectionKey = sectionCard[1][0]
                sectionName = paramDict["_sectionName"] % str(sectionKey)
                # Extract cards that might be referenced by other cards
                self.extractRefParams(outerSection, paramDict)

                self.outputSection(outerSection, sectionName)

                # make sure we remove section-specific refs.
                self.removeRefParams(paramDict)
            if "_section" in paramDict:
                del paramDict["_section"]

        self.outputListEnd(groupName)

    def createOutput(self):
        self.indent = 0
        # add XML header and stylesheet
        self.outList = ['<?xml version="1.0" encoding="UTF-8"?>',
            '<?xml-stylesheet version="1.0" type="text/xsl" href="PL9.xsl"?>']
        if not self.caseID:
            print("CASEID section missing, invalid input file")
            return

        # CASEID contains all other sections
        self.outputListStart(self.caseID[0])
        self.outputCards(self.caseID[1:], VeraInConverter.sectionNames[self.caseID[0]])

        # States are contained in their own list, with IDs to order them
        self.outputListStart("STATES")
        statesCount = 1
        for state in self.states:
            self.outputSection(state, "State_%d" % statesCount)
            statesCount += 1
        self.outputListEnd("STATES")

        # Always output core after states.
        if self.core:
            self.outputSection(self.core)

        # import ipdb; ipdb.set_trace()
        for section in self.cellSections:
            self.outputCellSection(self.cellSections[section])

        for section in self.sections:
            self.outputSection(section)

        self.outputListEnd(self.caseID[0])

    def parse(self, strng ):
        print( strng)
        tokens = None
        try:
            iniFile = open(strng, "r")
            iniData = "".join( iniFile.readlines() )
            bnf = self.inpfile_BNF()
            includebnf = self.include_BNF()
            afterIncludes = includebnf.transformString(iniData)
            # print(afterIncludes)
            tokens = bnf.parseString( afterIncludes, parseAll=True)
            # tokens.pprint()

        except pp.ParseException as err:
            print( err.line)
            print( " "*(err.column-1) + "^")
            print( err)

        iniFile.close()

        # try:
        self.createOutput()
        # except Exception as err:
        #     print(err)

        # print("\n".join(self.outList))
        print("Done")
        return tokens

    @staticmethod
    def add_arguments(parser):
        parser.add_argument("--in", default=None, help="path to .inp file to load", dest="fileToLoad")
        parser.add_argument("--out", default=None, help="path to .xml file to write", dest="fileToWrite")

# =============================================================================
# Main: Parse args and start server
# =============================================================================

if __name__ == "__main__":
    # Create argument parser
    argp = argparse.ArgumentParser(description="Convert VERAin .inp files to simulator input .xml files")

    # Add default arguments
    VeraInConverter.add_arguments(argp)
    args = argp.parse_args()
    converter = VeraInConverter()

    ini = converter.parse(args.fileToLoad)
    if ini and args.fileToWrite:
        outFile = open(args.fileToWrite, "w")
        outFile.write("\n".join(converter.outList))
        outFile.close()


