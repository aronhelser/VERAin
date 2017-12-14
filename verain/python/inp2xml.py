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
        "SHIFT": CASEID,
        # Simulator code config blocks
        "COBRATF": CASEID,
        "INSILICO": CASEID,
        "MPACT": CASEID,
        "BISON": CASEID,
        "MAMBA1D": CASEID,
        "TIAMAT": CASEID
    }

    cellSectionNames = ["ASSEMBLY", "CONTROL", "DETECTOR", "INSERT"]
    keywordSpace = 2
    inpbnf = None

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

            quoteStr = pp.quotedString.addParseAction(pp.removeQuotes)

            # keywords start an input card, two space indent
            keyWordDef = pp.Word( pp.alphas, pp.alphanums + "_" )
            spaceKeyWordDef = pp.White(" ", exact=VeraInConverter.keywordSpace).suppress() + keyWordDef
            # values or value lists, or indented sections complete the card
            valueDef = (quoteStr | pp.ZeroOrMore( floatnumber | pp.Word(nonsemi) ))
            valueDefEOL = valueDef + pp.OneOrMore(EOL)
            valueDefSemi = valueDef + semi
            # must be indented more than the keywords.
            indentedValueDef = pp.White(" ", min=(VeraInConverter.keywordSpace+1)).suppress() + valueDefEOL
            cardDef = pp.Group( spaceKeyWordDef + pp.Group(valueDefEOL + pp.Optional( pp.OneOrMore(pp.Group(indentedValueDef))) ) )
            # special handling for semi-separated-list of cards on one line for [STATE] blocks
            inlineCardDefSemi = pp.Group( keyWordDef + pp.Group(valueDefSemi) )
            inlineCardDefEOL = pp.Group( keyWordDef + pp.Group(valueDefEOL) )

            # section header complicated by possible inline cards on the same line.
            sectionHeader = lbrack + pp.oneOf( VeraInConverter.sectionNames.keys() ) + rbrack + \
                ( (pp.ZeroOrMore(inlineCardDefSemi | semi) + inlineCardDefEOL) | pp.ZeroOrMore(EOL) )

            # using Dict will allow retrieval of named data fields as attributes of the parsed results
            # this is a problem with [STATE] blocks, which can occur more than once.
            sectionDef = pp.Group( sectionHeader + pp.Dict( pp.ZeroOrMore( cardDef ) ) ^ EOL).setParseAction(
                self.handleSection
            )
            VeraInConverter.inpbnf = pp.Dict( pp.OneOrMore( sectionDef ) )

            VeraInConverter.inpbnf.ignore( comment)

        return VeraInConverter.inpbnf

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
                # taking the indicated value of the card there's a second colon, else get whole array for maps.
                argList[i] = refs[key][int(argSplit[2])] if len(argSplit) == 3 else refs[key]

    def outputParam(self, name, ptype, value):
        self.outList.append('%s<Parameter name="%s" type="%s" value="%s"/>' % (
            " " * self.indent, name, ptype, value) )

    def outputSingleCard(self, card, spec, paramName, refs=None):
        for outSpec in spec["_output"]:
            # "_name" is an override for the input paramName
            outName = outSpec["_name"] if "_name" in outSpec else paramName
            # type is modified for arrays
            if "_type" in outSpec:
                outType = outSpec["_type"] if outSpec["_pltype"] != "array" else "Array(%s)" % outSpec["_type"]
            else:
                outType = "none"
            if outSpec["_pltype"] == "parameter" or outSpec["_pltype"] == "array":
                if type(outSpec["_value"]) == list:
                    # make a copy
                    genValueList = outSpec["_value"][:]
                    # see if there are any args that need to be replaced with "_refs"
                    if refs:
                        self.replaceRefArgs(genValueList, refs)

                    # first item is method to call, the rest are args.
                    self.outputParam( outName, outType, genValueList[0](card[1], *genValueList[1:]))
                else:
                    self.outputParam( outName, outType, outSpec["_value"](card[1]))
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

                    print("GENREF", outName, refs[str(outName)])
            else:
                print("TODO", outName, outSpec["_pltype"])

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

    # Output a list of lists, with the inner lists derived from a single input card.
    def outputCardList(self, listCards, paramDict, refs):
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

    def outputCards(self, cards, paramDict):
        listCards = []
        listParamName = ""
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
                # lists - see if any existing cardlist has terminated and needs to be output.
                if listCards and (not ("_pltype" in spec and spec["_pltype"] == "list") or listParamName != paramName):
                    # handle the saved list of cards as a list.
                    self.outputCardList(listCards, paramDict, refs)
                    # reset the cardList
                    listCards = []
                    listParamName = ""

                # lists - gather cards first.
                if "_pltype" in spec and spec["_pltype"] == "list":
                    listParamName = paramName
                    listCards.append(card)
                elif paramName != sectionName or card[1][0] == sectionKey:
                    # output if it's not a section card, or if it is a section card, and the key matches.
                    self.outputSingleCard(card, spec, paramName, refs)
            else:
                print("TODO", paramName, card[1][0] )

        # if we're done and we still have a card list, output it.
        if listCards:
            self.outputCardList(listCards, paramDict, refs)


    # Start and end a list, sets indent for contents.
    def outputListStart(self, name):
        self.outList.append('%s<ParameterList name="%s">' % (" " * self.indent, name))
        self.indent += 2
    def outputListEnd(self, name=None):
        self.indent -= 2
        self.outList.append('%s</ParameterList>' % (" " * self.indent))

    def outputSection(self, section, inSectionName=None, ordered=None):
        sectionName = inSectionName if inSectionName else section[0]

        paramDict = VeraInConverter.sectionNames[section[0]]
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

                ordered = paramDict["_order"] if "_order" in paramDict else None
                self.outputSection(outerSection, sectionName, ordered)

                # make sure we remove section-specific refs.
                self.removeRefParams(paramDict)

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
            tokens = bnf.parseString( iniData, parseAll=True)
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


