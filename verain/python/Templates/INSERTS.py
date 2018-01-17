from __future__ import absolute_import, division, print_function

import copy
from Templates.Utils import *
# base for sections that have axial, rodmap, cells, ...
from Templates.CellMaps import CellMaps

_insertDiff = {
  "_groupName": "INSERTS",
  "_sectionName": "Insert_%s",
}

INSERT = copy.deepcopy(CellMaps)
INSERT.update(_insertDiff)
