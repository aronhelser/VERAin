import re
strng="INSILICO"
iniFile = open("../../scripts/Templates/" +strng + ".yml", "r")
data = "".join( iniFile.readlines() )
# quote all keywords
pat = re.compile(r'(\w*):')
data = pat.sub(r'"\1":', data)
#quote all values
pat = re.compile(r': (\w*)')
data = pat.sub(r': "\1",', data)
#switch "_content:"
pat = re.compile(r'"_content":')
data = pat.sub(r'    "_value": copy_value,', data)
# add output nesting
pat = re.compile(r':\n(\s+)"_pltype"', re.MULTILINE)
data = pat.sub(r': {\n\1"_output": [\n\1  {\n\1    "_pltype"', data)
pat = re.compile(r'\n(\s+)      "_value": copy_value,\n', re.MULTILINE)
data = pat.sub(r'\n\1      "_value": copy_value,\n\1    }\n\1  ]\n\1},', data)
#indent
pat = re.compile(r'"_type":')
data = pat.sub(r'    "_type":', data)
pat = re.compile(r'"_do":')
data = pat.sub(r'    # "_do":', data)
pat = re.compile(r'  - ')
data = pat.sub(r'    #  - ', data)
# fixup header
pat = re.compile('"' + strng + '''":( {)?
''', re.MULTILINE)
data = pat.sub('' + strng + ''' = {
  "_content": {
''', data)
data += '''
  }
}
'''

outF = open(strng + "x.py", "w")
outF.write(data)
