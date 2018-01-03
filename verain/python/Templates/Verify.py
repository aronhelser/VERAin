from __future__ import absolute_import, division, print_function

def is_double(toks, index=None):
  if index == None:
    val = toks[0]
  else:
    val = toks[index]
  # automatic converter might produce ints or floats (double-precision in python)
  if type(val) != float:
    raise ValueError("expected double got" + type(val))
  # print("verified double", val)

def is_literal(toks, verifVal, index=None):
  if index == None:
    val = toks[0]
  else:
    val = toks[index]
  if val != verifVal:
    raise ValueError("expected '%s' got '%s'" % (str(verifVal), str(val)))
