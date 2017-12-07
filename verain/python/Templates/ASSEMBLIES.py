from __future__ import absolute_import, division, print_function

from Templates.Utils import *

ASSEMBLY = {
  "_groupName": "ASSEMBLIES",
  "_pltype": "list",
  "_sectionParams": ["axial"],
  "_sectionName": "Assembly_%s",
  "_refParams": ["npin"],
  "_content": {
      # "_do":
      #  - setdb MAIN_DB
      #  - namesunique %ASSEMBLY/*/$/%axial
      #  - isinmaps %ASSEMBLY/*/$/%axial,CORE/@assm_map

      # _tr:
      #   _name: _loop
      #   _content: %ASSEMBLY/*/$/%axial
      # Assembly_(_loop)"": {
          # "_pltype": "list",
          # "_do":
          #  - setdb MAIN_DB
          #  - setvar _path,%ASSEMBLY/*/$/%axial/$(_loop),apply=>&findfirst
          #  - getvar _path,apply=>&pathlevel,arg=>3
          #  - cellsmaps %ASSEMBLY/$(_path)/%rodmap,%ASSEMBLY/$(_path)/%cell,%ASSEMBLY/$(_path)/$npin,%ASSEMBLY/$(_path)/%axial/$(_loop),matsearch=>%ASSEMBLY/$(_path)/%mat/*"":%ASSEMBLY/$(_path)/%fuel/*"":CORE/%mat/*
    "fuel": {
      "_pltype": "list",
      "_name": "Fuels",
      "_listName": "Fuel_%s",
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
          "_name": "thden",
          "_pltype": "parameter",
          "_type": "double",
          "_value": [copy_value, 2],
        },
      ]
    },
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
          "_value": [copy_array_before_val, '/', slice(1, None)],
        },
        {
          "_name": "num_rings",
          "_pltype": "parameter",
          "_type": "int",
          # "_do":
          #  - value (_lgrid)
          "_value": [len_array_after_val, '/'],
        },
      ]
    },
    "lattice": {
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
    "ppitch": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy %ASSEMBLY/$(_path)/$ppitch
          "_value": copy_value,
        }
      ]
    },
    "lower_nozzle": {
      "_output": [
        {
          "_name": "lower_nozzle_comp",
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy %ASSEMBLY/$(_path)/@"lower_nozzle":0
          "_value": [copy_value, 0],
        },
        {
          "_name": "lower_nozzle_height",
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy %ASSEMBLY/$(_path)/@"lower_nozzle":1
          "_value": [copy_value, 1],
        },
        {
          "_name": "lower_nozzle_mass",
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy %ASSEMBLY/$(_path)/@"lower_nozzle":2
          "_value": [copy_value, 2],
        }
      ]
    },
    "upper_nozzle": {
      "_output": [
        {
          "_name": "upper_nozzle_comp",
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy %ASSEMBLY/$(_path)/@"upper_nozzle":0
          "_value": [copy_value, 0],
        },
        {
          "_name": "upper_nozzle_height",
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy %ASSEMBLY/$(_path)/@"upper_nozzle":1
          "_value": [copy_value, 1],
        },
        {
          "_name": "upper_nozzle_mass",
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy %ASSEMBLY/$(_path)/@"upper_nozzle":2
          "_value": [copy_value, 2],
        }
      ]
    },
    "grid_axial": {
      "_output": [
        {
          "_name": "grid_elev",
          "_pltype": "array",
          "_type": "double",
          # "_do":
          #  - copyarray %ASSEMBLY/$(_path)/@grid_axial,select=>odd
          "_value": [copy_array, slice(1, None, 2)]
        },
        {
          "_name": "grid_map",
          "_pltype": "array",
          "_type": "string",
          # "_do":
          #  - copyarray %ASSEMBLY/$(_path)/@grid_axial,select=>even
          "_value": [copy_array, slice(0, None, 2)]
        }
      ]
    },
    "grid": {
      "_pltype": "list",
      "_name": "SpacerGrids",
      "_listName": "Grid_%s",
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
          "_name": "material",
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy %ASSEMBLY/$(_path)/%grid/@(_lgrid)"":0
          "_value": [copy_value, 1],
        },
        {
          "_name": "mass",
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy %ASSEMBLY/$(_path)/%grid/@(_lgrid)"":2
          "_value": [copy_value, 3],
        },
        {
          "_name": "height",
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy %ASSEMBLY/$(_path)/%grid/@(_lgrid)"":1
          "_value": [copy_value, 2],
        },
        # The old way of specifying gridloss.  Still read in for backwards compatibility, but this will be removed
        # in the future.
        {
          "_name": "gridloss_old",
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy %ASSEMBLY/$(_path)/%grid/@(_lgrid)"":3
          "_value": [copy_value, 4],
        },
        # {
        #   "_name": "gridloss",
        #   "_pltype": "parameter",
        #   "_type": "double",
        #   # "_do":
        #   #  - copy %ASSEMBLY/$(_path)/%grid/$(_lgrid)^/$loss
        #   "_value": copy_value,
        # },
        # {
        #   "_name": "gridblock",
        #   "_pltype": "parameter",
        #   "_type": "double",
        #   # "_do":
        #   #  - copy %ASSEMBLY/$(_path)/%grid/$(_lgrid)^/$blockage
        #   "_value": copy_value,
        # }
      ]
    },

    "gap": {
      "_output": [
        {
          "_name": "gapw",
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy %ASSEMBLY/$(_path)/@"gap":0
          "_value": [copy_value, 0],
        },
        {
          "_name": "gapn",
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy %ASSEMBLY/$(_path)/@"gap":1
          "_value": [copy_value, 1],
        }
      ]
    },
    "channel_box": {
      "_output": [
        {
          "_name": "chanmat",
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy %ASSEMBLY/$(_path)/@"channel_box":0,existspath=>%ASSEMBLY/$(_path)/%mat/*"":CORE/%mat/*
          "_value": [copy_value, 0, "TODOEXISTS"],
        },
        {
          "_name": "chanth",
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy %ASSEMBLY/$(_path)/@"channel_box":1
          "_value": [copy_value, 1],
        },
        {
          "_name": "chanrad",
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy %ASSEMBLY/$(_path)/@"channel_box":2
          "_value": [copy_value, 2],
        },
        {
          "_name": "cornerth",
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy %ASSEMBLY/$(_path)/@"channel_box":3
          "_value": [copy_value, 3],
        },
        {
          "_name": "cornerlen",
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy %ASSEMBLY/$(_path)/@"channel_box":4
          "_value": [copy_value, 4],
        }
      ]
    },
  }
}

