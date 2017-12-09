from __future__ import absolute_import, division, print_function

import copy
from Templates.Utils import *
# base for sections that have axial, rodmap, cells, ...
from Templates.CellMaps import CellMaps

_detectorDiff = {
  "_groupName": "DETECTORS",
  "_sectionName": "Detector_%s",
}

DETECTOR = copy.deepcopy(CellMaps)
DETECTOR.update(_detectorDiff)
