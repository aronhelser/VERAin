from __future__ import absolute_import, division, print_function
import itertools
import pyparsing as pp

# old school flatten: http://rightfootin.blogspot.com/2006/09/more-on-python-flatten.html
# add pp.ParseResults as a list type to flatten.
def flatten(l, ltypes=(list, tuple, pp.ParseResults)):
    ltype = type(l)
    l = list(l)
    i = 0
    while i < len(l):
        while isinstance(l[i], ltypes):
            if not l[i]:
                l.pop(i)
                i -= 1
                break
            else:
                l[i:i + 1] = l[i]
        i += 1
    return ltype(l)

# transpose an octant map so [[1], [2,3]] turns into [[1, 2], [3]]
def transpose(m):
  # we can't assume a square matrix, so must resort to nested for loops
  mout = []
  for j in range(len(m)):
    for i in range(len(m[j])):
      if i >= len(mout):
        mout.append([])
      mout[i].append(m[j][i])
  return mout

def octToQuadMap(a):
  # mirror octant
  b = transpose(a)
  # cut off duplicate element along diagonal
  c = [b[i][1:] for i in range(len(b))]
  # combine into list - convert parse results into python list
  d = [list(a[i]) + c[i] if i < len(c) else a[i] for i in range(len(a))]
  return d

def quadToFullMap(a, symmetry):
  # optimization, drop first element, reverse: [1:][::-1] slice
  # is the same as [:0:-1] single slice

  # the input is the bottom-right quadrant
  # make the bottom left
  if symmetry == "rot":
    # drop the first row, which after transposition is a duplicate
    # of the bottom-right's first column
    bottom_right = transpose(a[:0:-1])
  else:
    bottom_right = [list(row)[:0:-1] for row in a]
  # mirror symmetry - make reversed copies of quad
  # drop the duplicate center elem, reverse
  bottom = [list(bottom_right[i]) + list(a[i]) for i in range(len(a))]
  if symmetry == "rot":
    # to get a rotated version, we need to reverse both rows and columns,
    # dropping the duplicate
    full = [ row[::-1] for row in bottom[:0:-1] ] + bottom
  else:
    # same thing to get a mirror copy for the top half
    full = bottom[:0:-1] + bottom
  return full

# return an array of values from a given token list
def extract_array(toks, inSlice=slice(0, None)):
  return flatten(toks)[inSlice]

# Given a set of tokens, see
def tag_used_in(toks, keyList):
  # source = set(flatten(toks))
  # the card's tag is the first value
  tag = str(toks[0])
  compare = set(keyList)
  if tag in compare:
    return True
  return False

# extract values from token lists:

def copy_value(toks, index=0):
  return toks[index]

def copy_value_mult(toks, index, mult):
  return toks[index] * mult

def copy_array(toks, inSlice=slice(0, None)):
  # want a comma-delimited list, surrounded by {}
  # flatten nested lists for multi-line cards
  return "{%s}" % ",".join(str(num) for num in flatten(toks)[inSlice])

def copy_array_after_val(toks, val, inSlice=slice(0, None)):
  outList = flatten(toks)
  indices = [i for i, j in enumerate(toks) if j == val]
  if indices:
    # grab the list after the first val we found.
    outList = outList[indices[0]+1:]
  return copy_array(outList, inSlice)

def copy_array_before_val(toks, val, inSlice=slice(0, None)):
  outList = flatten(toks)
  indices = [i for i, j in enumerate(toks) if j == val]
  if indices:
    # grab the list before the first val we found.
    outList = outList[:indices[0]]
  return copy_array(outList, inSlice)

def len_array_after_val(toks, val, inSlice=slice(0, None)):
  outList = flatten(toks)
  indices = [i for i, j in enumerate(toks) if j == val]
  if indices:
    # grab the list after the first val we found.
    outList = outList[indices[0]+1:]
    return len(outList)
  return 0

def toCelsius(toks):
  if len(toks) != 2 or not(toks[1] in ["F", "C", "K"]):
    raise ValueError("Invalid temperature")
  val = toks[0]
  units = toks[1]

  # Tc=(Tf-32)/1.8
  # Tc=Tk-273.15
  # Tc=Tc
  if units == "C":
    return val
  elif units == "F":
    return (val - 32.0) / 1.8
  elif units == "K":
    return val - 273.15

def toKelvin(toks):
  return toCelsius(toks) + 273.15

# a core map is an array, but expanded to match the
# occupied cells in the core_shape map.
def core_map(toks, core_size, symmetry="rot"):
  # special case, 42*3, means array of length 42, filled with '3'
  # explicitly parsed by mapProductDef in parser.
  if (len(toks) == 3) and type(toks[0]) is int \
    and type(toks[1]) is str \
    and toks[1] == "*":
    # print("Repeat array", toks[0], toks[1])
    repeat = toks[0]
    val = toks[2]

    return copy_array([val] * repeat)

  if core_size > 1 and len(toks[0]) == 1:
    quad = octToQuadMap(toks)
  else:
    quad = toks
  if core_size > 1 and len(quad[0]) < core_size:
    full = quadToFullMap(quad, symmetry)
  else:
    full = quad
  return copy_array(full)

def assembly_map(toks, num_pins):
  return core_map(toks[1:], num_pins)

# what symbols are used in this map? Includes empty tokens, like '-' or '0'
def extract_map_cells(toks, start):
  vals = extract_array(toks, slice(start, None))
  uniqueVals = set(vals)
  # need to make sure everything is a string, not an integer.
  return set([str(x) for x in uniqueVals])
