from __future__ import absolute_import, division, print_function
import itertools
from functools import reduce
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

def isDouble(str):
    try:
      a = float( str )
      return True
    except:
      return False

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

def copy_value_if_not(toks, exclude, index=0):
  if toks[index] != exclude:
    return toks[index]
  return None

def copy_array(toks, inSlice=slice(0, None)):
  # want a comma-delimited list, surrounded by {}
  # flatten nested lists for multi-line cards
  return "{%s}" % ",".join(str(num) for num in flatten(toks)[inSlice])

def copy_array_after_val(toks, val, inSlice=slice(0, None)):
  outList = flatten(toks)
  indices = [i for i, j in enumerate(outList) if j == val]
  if indices:
    # grab the list after the first val we found.
    outList = outList[indices[0]+1:]
    return copy_array(outList, inSlice)
  return None

def copy_array_before_val(toks, val, inSlice=slice(0, None)):
  outList = flatten(toks)
  indices = [i for i, j in enumerate(outList) if j == val]
  if indices:
    # grab the list before the first val we found.
    outList = outList[:indices[0]]
  return copy_array(outList, inSlice)

def len_array_after_val(toks, val, inSlice=slice(0, None)):
  outList = flatten(toks)
  indices = [i for i, j in enumerate(outList) if j == val]
  if indices:
    # grab the list after the first val we found.
    outList = outList[indices[0]+1:]
    return len(outList)
  return None

# params are name=val after the last '/' in a list
def extract_param(toks, name):
  outList = flatten(toks)
  indices = [i for i, j in enumerate(outList) if j == '/']
  if indices:
    # grab after the last value.
    outList = outList[indices[-1]+1:]
    # see if "name=" matches
    prefix = "%s=" % name
    lenPrefix = len(prefix)
    for pair in outList:
      if pair[:lenPrefix] == prefix:
        return pair[lenPrefix:]
  return None

# the fuel definition has three separate parts, and
# the last two are optional. Handle all in one place.
def fuel_array(toks, outKey):
  outList = flatten(toks)
  indices = [i for i, j in enumerate(outList) if j == '/']
  # three parts, split by slash
  part1 = None # default list, but thden is optional
  part2 = None # fuel list, optional
  part3 = None # gad list, optional

  # first two values are always present, handled separately - strip them off.
  part1 = outList[2:] if len(indices) == 0 else outList[2:indices[0]]
  if len(indices) == 1:
    part2 = outList[indices[0]+1:]
  elif len(indices) == 2:
    part2 = outList[indices[0]+1:indices[1]]
    part3 = outList[indices[1]+1:]
    if part3 and len(part3) != 1:
      raise ValueError("Too many values in fuel 'gad' definition")
  else:
    raise ValueError("Too many '/' in fuel definition")

  fuelNames = []
  fuelEnrich = []
  if part2:
    # split fuel=val tokens into fuel, val lists.
    # can also be listed as 'fuel val' pairs
    part2 = flatten([str(val).split('=') for val in part2])
    # First fuel defaults to u-235, if only a number is provided
    if isDouble(part2[0]):
        fuelNames = ["u-235"] + part2[1::2]
        fuelEnrich = part2[0::2]
    else:
        fuelNames = part2[0::2]
        fuelEnrich = part2[1::2]

  gadMat = None
  gadFrac = None
  if part3:
    vals = str(part3[0]).split('=')
    if len(vals) != 2:
      raise ValueError("Need single '=' in fuel gad definition")
    gadMat = vals[0]
    gadFrac = vals[1]

  # last value in first section, optional.
  if outKey == "thden":
    if part1:
      return part1[0]
    else:
      return None
  # part 2 outputs:
  if outKey == "fuel_names":
    if fuelNames:
      return copy_array(fuelNames)
    else:
      return None
  if outKey == "enrichments":
    if fuelNames:
      return copy_array(fuelEnrich)
    else:
      return None
  # part 3 outputs:
  if outKey == "gad_mat":
      return gadMat
  if outKey == "gad_frac":
    return gadFrac

def cell_type(toks, fuelNames):
  # first extract the material names used
  matNames = copy_array_after_val(toks, '/')
  # if any fuel name appears in the list, this is a fuel cell.
  if fuelNames:
    for fuel in fuelNames:
      if fuel in matNames:
        return "fuel"
  return "other"

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
def core_map(toks, coreSize, coreStats, symmetry="rot"):
  totalOnes, onesPerRow = coreStats
  # special case, 42*3, means array of length 42, filled with '3'
  # explicitly parsed by mapProductDef in parser.
  if (len(toks) == 3) and type(toks[0]) is int \
    and type(toks[1]) is str \
    and toks[1] == "*":
    # print("Repeat array", toks[0], toks[1])
    repeat = toks[0]
    val = toks[2]
    if repeat != totalOnes:
      raise ValueError("Core map repeated count (%d) doesn't match core_shape definition (%d)" % (repeat, totalOnes))

    return copy_array([val] * repeat)

  if coreSize > 1 and len(toks[0]) == 1:
    quad = octToQuadMap(toks)
  else:
    quad = toks
  # onesPerRow has count of elements needed per row.
  if coreSize > 1 and len(quad) < len(onesPerRow):
    full = quadToFullMap(quad, symmetry)
  else:
    full = quad
  if len(full) != len(onesPerRow):
    raise ValueError("Map rows inconsistent, expect %d, got %d" % (len(full), len(onesPerRow)))
  for i, count in enumerate(onesPerRow):
    if len(full[i]) != count:
      raise ValueError("Map row %d inconsistent, expect %d, got %d" % (i, len(full[i]), count))
  return copy_array(full)

def assembly_map(toks, numPins):
  stats = (numPins, [numPins] * numPins)
  return core_map(toks[1:], numPins, stats)

# what symbols are used in this map? Includes empty tokens, like '-' or '0'
def extract_map_cells(toks, start):
  vals = extract_array(toks, slice(start, None))
  uniqueVals = set(vals)
  # need to make sure everything is a string, not an integer.
  return set([str(x) for x in uniqueVals])

# what tags are used? Combined from a list
def extract_tag(toks, index):
  val = toks[index]
  return set([str(val)])

def extract_core_shape(toks):
  # we need to know the total number of '1' (occupied cells)
  # possibly also the number of '1' per row
  onesPerRow = []
  for row in toks:
    onesPerRow.append(len([a for a in row if a == 1]))

  totalOnes = reduce(lambda x, y: x+y, onesPerRow, 0)
  return (totalOnes, onesPerRow)

# almost: [copy_array_before_val, '/', slice(3, None, 2)],
# but we need a default of 1 if there's a name with no frac.
def mat_fracs(toks):
  val = '/'
  # strip name, density
  outList = flatten(toks)[2:]
  indices = [i for i, j in enumerate(outList) if j == val]
  if indices:
    # grab the list before the first val we found.
    outList = outList[:indices[0]]
  # if there's only a name, the default frac is 1
  if len(outList) == 1:
    return copy_array([1])
  # otherwise copy the second value in each pair.
  return copy_array(outList, slice(1, None, 2))
