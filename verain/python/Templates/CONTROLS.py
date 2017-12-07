from __future__ import absolute_import, division, print_function

from Templates.Utils import *

CONTROL = {
  "_groupName": "CONTROLS",
  "_pltype": "list",
  "_sectionParams": ["axial"],
  "_sectionName": "Control_%s",
  "_refParams": ["npin"],
  "_content": {
#   _do:
#     - setdb MAIN_DB
#     - namesunique %INSERT/*/$/%axial
#     - isinmaps %INSERT/*/$/%axial,CORE/@insert_map

#   _tr:
#     _name: _loop
#     _content: %INSERT/*/$/%axial

# #    - rodmap INSERT/%axial,basename=>Insert_,coremap=>CORE/@insert_map,matsearch=>INSERT/%mat/*:CORE/%mat/*
    # Insert_(_loop)"": {
    #   "_output": [
    #     {
    #       "_pltype": "list",
          # "_do":
          #  - setdb MAIN_DB
          #  - setvar _path,%INSERT/*/$/%axial/$(_loop),apply=>&findfirst
          #  - getvar _path,apply=>&pathlevel,arg=>3
          #  - cellsmaps %INSERT/$(_path)/%rodmap,%INSERT/$(_path)/%cell,%INSERT/$(_path)/$npin,%INSERT/$(_path)/%axial/$(_loop),matsearch=>%INSERT/$(_path)/%mat/*"":CORE/%mat/*
    "cell": {
      "_pltype": "list",
      "_name": "Cells",
      "_listName": "Cell_%s",
      "_output": [
        {
          "_name": "label",
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - value (_lgrid)
          "_value": [copy_value, 0],
        },
        {
          "_name": "mats",
          "_pltype": "array",
          "_type": "string",
          "_value": [copy_array_after_val, '/'],
        },
        {
          "_name": "radii",
          "_pltype": "array",
          "_type": "double",
          # have to skip the cell label
          "_value": [copy_array_before_val, '/', slice(1, None)],
        },
        {
          "_name": "num_rings",
          "_pltype": "parameter",
          "_type": "int",
          # match length of mats array.
          "_value": [len_array_after_val, '/'],
        },
      ]
    },
    "rodmap": {
      "_pltype": "list",
      "_name": "CellMaps",
      "_listName": "CellMap_%s",
      "_output": [
        {
          "_name": "label",
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - value (_lgrid)
          "_value": [copy_value, 0],
        },
        {
          "_name": "cell_map",
          "_pltype": "array",
          "_type": "string",
          "_value": [assembly_map, "ref:npin"],
        },
      ]
    },
    "axial": {
      "_matchSection": True,
      "_output": [
        {
          "_name": "label",
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - value (_loop)
          "_value": [copy_value, 0],
        },
        {
          "_name": "axial_labels",
          "_pltype": "array",
          "_type": "string",
          # "_do":
          #  - copyarray %ASSEMBLY/$(_path)/%axial/$(_loop),select=>odd
          "_value": [copy_array, slice(2, None, 2)],
        },
        {
          "_name": "axial_elevations",
          "_pltype": "array",
          "_type": "double",
          # "_do":
          #  - copyarray %ASSEMBLY/$(_path)/%axial/$(_loop),select=>even
          "_value": [copy_array, slice(1, None, 2)],
        }
      ]
    },
    "Materials": {
      "_output": [
        {
          "_pltype": "list",
          # "_do":
          #  - matmap Material_,%ASSEMBLY/$(_path)/%mat/*
          "_value": copy_value,
        }
      ]
    },
    "title": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy %ASSEMBLY/$(_path)/$title
          "_value": copy_value,
        }
      ]
    },
    "npin": {
      "_output": [
        {
          "_name": "num_pins",
          "_pltype": "parameter",
          "_type": "int",
          # "_do":
          #  - copy %ASSEMBLY/$(_path)/$npin
          "_value": copy_value,
        }
      ]
    },
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
}
