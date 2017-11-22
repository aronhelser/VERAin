from __future__ import absolute_import, division, print_function

import pyparsing as pp
import os, argparse

sectionNames = [
    "CASEID",
    "CORE",
    "STATE",
    "ASSEMBLY",
    "INSERT",
    "CONTROL",
    "DETECTOR",
    "EDITS",
    "COUPLING",
    "SHIFT",
    # Simulator code config blocks
    "COBRATF",
    "INSILICO",
    "MPACT"
]

keywordSpace = 2
inpbnf = None
indentStack = [1]
def inpfile_BNF():
    global inpbnf, indentStack

    if not inpbnf:
        # allow us to detect separate lines, but still ignore space between words
        pp.ParserElement.setDefaultWhitespaceChars(' \t')

        # punctuation
        lbrack = pp.Literal("[").suppress()
        rbrack = pp.Literal("]").suppress()
        # equals = pp.Literal("=").suppress()
        semi   = pp.Literal(";").suppress()
        EOL = pp.LineEnd().suppress()
        # nonrbrack = "".join( [ c for c in pp.printables if c != "]" ] ) + " \t"

        # ignore comments completely
        comment = pp.Literal("!") + pp.Optional( pp.restOfLine )


        sectionDef = lbrack + pp.oneOf( sectionNames ) + rbrack + pp.ZeroOrMore(EOL)

        # keywords start an input card, two space indent
        keyWordDef = pp.White(" ", exact=keywordSpace).suppress() + pp.Word( pp.alphas, pp.alphanums + "_" )
        # values or value lists, or indented sections complete the card
        valueDef = (pp.quotedString | pp.ZeroOrMore( pp.Word(pp.printables) )) + pp.OneOrMore(EOL)
        # must be indented more than the keywords.
        indentedValueDef = pp.White(" ", min=(keywordSpace+1)).suppress() + valueDef
        cardDef = keyWordDef + pp.Group(valueDef + pp.Optional( pp.OneOrMore(pp.Group(indentedValueDef))) )

        # using Dict will allow retrieval of named data fields as attributes of the parsed results
        # this is a problem with [STATE] blocks, which can occur more than once.
        inpbnf = pp.Dict( pp.OneOrMore( pp.Group( sectionDef + pp.Dict( pp.ZeroOrMore( pp.Group( cardDef ) ) ) ^ EOL) ) )

        inpbnf.ignore( comment)

    return inpbnf


def test( strng ):
    print( strng)
    try:
        iniFile = open(strng, "r")
        iniData = "".join( iniFile.readlines() )
        bnf = inpfile_BNF()
        tokens = bnf.parseString( iniData )
        tokens.pprint()

    except pp.ParseException as err:
        print( err.line)
        print( " "*(err.column-1) + "^")
        print( err)

    iniFile.close()
    print()
    return tokens

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
    add_arguments(argp)
    args = argp.parse_args()

    ini = test(args.fileToLoad)
    print( "ini.CASEID =", ini.CASEID)
    print( "ini.STATE.power =", ini.STATE.power)

