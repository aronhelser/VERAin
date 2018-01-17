from __future__ import absolute_import, division, print_function

import copy
from Templates.Utils import *
# base for sections that have axial, rodmap, cells, ...
from Templates.CellMaps import CellMaps

_controlDiff = {
  "_groupName": "CONTROLS",
  "_sectionName": "Control_%s",
}

CONTROL = copy.deepcopy(CellMaps)
CONTROL.update(_controlDiff)

_controlContentDiff = {
    "stroke": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy %CONTROL/$(_path)/@"stroke":0
          "_value": [copy_value, 0],
        },
        {
          "_name": "maxstep",
          "_pltype": "parameter",
          "_type": "int",
          # "_do":
          #  - copy %CONTROL/$(_path)/@"stroke":1
          "_value": [copy_value, 1],
        }
      ]
    },
    "blade": {
      "_output": [
        {
          "_name": "ntube",
          "_pltype": "parameter",
          "_type": "int",
          # "_do":
          #  - copy %CONTROL/$(_path)/@"blade":0
          "_value": [copy_value, 0],
        },
        {
          "_name": "tubecell",
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy %CONTROL/$(_path)/@"blade":1,existspath=>%CONTROL/$(_path)/%cell/*
          "_value": [copy_value, 1, "TODOEXISTS"],
        },
        {
          "_name": "bladespan",
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy %CONTROL/$(_path)/@"blade":2
          "_value": [copy_value, 2],
        },
        {
          "_name": "bladeth",
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy %CONTROL/$(_path)/@"blade":3
          "_value": [copy_value, 3],
        },
        {
          "_name": "bladerad",
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy %CONTROL/$(_path)/@"blade":4
          "_value": [copy_value, 4],
        },
        {
          "_name": "bladesheath",
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy %CONTROL/$(_path)/@"blade":5
          "_value": [copy_value, 5],
        },
        {
          "_name": "bladewing",
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy %CONTROL/$(_path)/@"blade":6
          "_value": [copy_value, 6],
        },
        {
          "_name": "blademat",
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy %CONTROL/$(_path)/@"blade":7,existspath=>%CONTROL/$(_path)/%mat/*"":CORE/%mat/*
          "_value": [copy_value, 7, "TODOEXISTS"],
        }
      ]
    },
}
CONTROL["_content"].update(_controlContentDiff)
