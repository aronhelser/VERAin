from __future__ import absolute_import, division, print_function

from Templates.Utils import *

CellMaps = {
  # "_groupName": "INSERTS",
  "_pltype": "list",
  "_sectionParams": ["axial"],
  # "_sectionName": "Insert_%s",
  "_refParams": ["npin"],
  "_order": ["axial", "rodmap", "fuel", "cell"],
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
      "_condition": [tag_used_in, "ref:cell_map"],
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
        {
          "_name": "type",
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - value (_lgrid)
          "_value": [cell_type, "ref:Fuels"],
        },
      ]
    },
    "rodmap": {
      "_pltype": "list",
      "_name": "CellMaps",
      "_listName": "CellMap_%s",
      # only output rodmap if it's used in the "axial_labels"
      "_condition": [tag_used_in, "ref:axial_labels"],
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
          "_refParam": [extract_map_cells, 1],
          "_value": [assembly_map, "ref:npin:0"],
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
          "_refParam": [extract_array, slice(2, None, 2)],
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
    "mat": {
      "_pltype": "list",
      "_name": "Materials",
      "_listName": "Material_%s",
      "_output": [
        {
          "_name": "key_name",
          "_pltype": "parameter",
          "_type": "string",
          "_value": [copy_value, 0],
        },
        {
          "_name": "density",
          "_pltype": "parameter",
          "_type": "double",
          "_value": [copy_value, 1],
        },
        {
          "_name": "mat_fracs",
          "_pltype": "array",
          "_type": "double",
          "_optional": True,
          "_value": [copy_array_before_val, '/', slice(3, None, 2)],
        },
        {
          "_name": "mat_names",
          "_pltype": "array",
          "_type": "string",
          "_optional": True,
          "_value": [copy_array_before_val, '/', slice(2, None, 2)],
        },
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
  }
}
