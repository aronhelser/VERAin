from __future__ import absolute_import, division, print_function

from Templates.Utils import *

CORE = {
  "_pltype": "list",
  # "_do":
  #   - setdb MAIN_DB
  "_refParams": ["size"],
  "_content": {
    "op_date": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #   - copy CORE/$op_date
          "_value": copy_value,
        }
      ]
    },
    "rated": {
      "_output": [
        {
          "_name": "rated_power",
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #   - copy CORE/@"rated":0
          "_value": [copy_value, 0],
        },
        {
          "_name": "rated_flow",
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #   - copy CORE/@"rated":1,apply=>$_[0]*125.9978
          "_value": [copy_value_mult, 1, 125.9978],
        }
      ]
    },
    "rcs_volume": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #   - copy CORE/@rcs_volume
          "_value": copy_value,
        }
      ]
    },
    "name": {
      "_output": [
        {
          "_name": "core_name",
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #   - copy CORE/$name
          "_value": copy_value,
        }
      ]
    },
    "size": {
      "_output": [
        {
          "_name": "core_size",
          "_pltype": "parameter",
          "_type": "int",
          # "_do":
          #   - copy CORE/$size
          "_value": copy_value,
        }
      ]
    },
    "unit": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #   - copy CORE/$unit
          "_value": copy_value,
        }
      ]
    },
    "cycle": {
      "_output": [
        {
          "_name": "cycle_num",
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #   - copy CORE/$cycle
          "_value": copy_value,
        }
      ]
    },
    "apitch": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #   - copy CORE/$apitch
          "_value": copy_value,
        }
      ]
    },
    "baffle": {
      "_output": [
        {
          "_name": "baffle_thick",
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #   - copy CORE/@"baffle":2
          "_value": [copy_value, 2],
        },
        {
          "_name": "baffle_gap",
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #   - copy CORE/@"baffle":1
          "_value": [copy_value, 1],
        },
        {
          "_name": "baffle_mat",
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #   - copy CORE/@"baffle":0
          "_value": [copy_value, 0],
        }
      ]
    },
    "pad": {
      "_output": [
        {
          "_name": "pad_mat",
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #   - copy CORE/@"pad":0
          "_value": [copy_value, 0],
        },
        {
          "_name": "pad_inner_radius",
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #   - copy CORE/@"pad":1
          "_value": [copy_value, 1],
        },
        {
          "_name": "pad_outer_radius",
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #   - copy CORE/@"pad":2
          "_value": [copy_value, 2],
        },
        {
          "_name": "pad_arc",
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #   - copy CORE/@"pad":3
          "_value": [copy_value, 3],
        },
        {
          "_name": "pad_azi_locs",
          "_pltype": "array",
          "_type": "double",
          # "_do":
          #   - copyarray CORE/@pad,start=>4
          "_value": [copy_array, slice(4, None)],
        }
      ]
    },
    "vessel": {
      "_output": [
        {
          "_name": "vessel_mats",
          "_pltype": "array",
          "_type": "string",
          # "_do":
          #   - copyarray CORE/@vessel,start=>0,stride=>2
          "_value": [copy_array, slice(0, None, 2)],
        },
        {
          "_name": "vessel_radii",
          "_pltype": "array",
          "_type": "double",
          # "_do":
          #   - copyarray CORE/@vessel,start=>1,stride=>2
          "_value": [copy_array, slice(1, None, 2)],
        }
      ]
    },
    "hole": {
      "_output": [
        {
          "_name": "hole_x",
          "_pltype": "array",
          "_type": "double",
          # "_do":
          #   - copyarray CORE/@hole,start=>0,stride=>3
          "_value": [copy_array, slice(0, None, 3)],
        },
        {
          "_name": "hole_y",
          "_pltype": "array",
          "_type": "double",
          # "_do":
          #   - copyarray CORE/@hole,start=>1,stride=>3
          "_value": [copy_array, slice(1, None, 3)],
        },
        {
          "_name": "hole_radius",
          "_pltype": "array",
          "_type": "double",
          # "_do":
          #   - copyarray CORE/@hole,start=>2,stride=>3
          "_value": [copy_array, slice(2, None, 3)],
        }
      ]
    },
    "assm_map": {
      "_output": [
        {
          "_pltype": "array",
          "_type": "string",
          # "_do":
          #   - coremapmap CORE/$size,CORE/@core_shape,CORE/@assm_map,CORE/$bc_sym
          "_value": [core_map, "ref:size"],
        }
      ]
    },
    "rotate_map": {
      "_output": [
        {
          "_pltype": "array",
          "_type": "int",
          # "_do":
          #   - coremapmap CORE/$size,CORE/@core_shape,CORE/@rotate_map,CORE/$bc_sym,expand=>0,ignore=>0
          "_value": [core_map, "ref:size"],
        }
      ]
    },
    "insert_map": {
      "_output": [
        {
          "_pltype": "array",
          "_type": "string",
          # "_do":
          #   - coremapmap CORE/$size,CORE/@core_shape,CORE/@insert_map,CORE/$bc_sym
          "_value": [core_map, "ref:size"],
        }
      ]
    },
    "det_map": {
      "_output": [
        {
          "_pltype": "array",
          "_type": "string",
          # "_do":
          #   - coremapmap CORE/$size,CORE/@core_shape,CORE/@det_map,CORE/$bc_sym
          "_value": [core_map, "ref:size"],
        }
      ]
    },
    "crd_map": {
      "_output": [
        {
          "_pltype": "array",
          "_type": "string",
          # "_do":
          #   - coremapmap CORE/$size,CORE/@core_shape,CORE/@crd_map,CORE/$bc_sym
          "_value": [core_map, "ref:size"],
        }
      ]
    },
    "crd_bank": {
      "_output": [
        {
          "_pltype": "array",
          "_type": "string",
          # "_do":
          #   - coremapmap CORE/$size,CORE/@core_shape,CORE/@crd_bank,CORE/$bc_sym
          "_value": [core_map, "ref:size"],
        }
      ]
    },
    "core_shape": {
      "_output": [
        {
          "_name": "shape",
          "_pltype": "array",
          "_type": "int",
          # "_do":
          #   - copy CORE/@core_shape
          "_value": copy_array,
        }
      ]
    },
    "lower_plate": {
      "_output": [
        {
          "_name": "lower_thick",
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #   - copy CORE/@"lower_plate":1
          "_value": [copy_value, 1],
        },
        {
          "_name": "lower_mat",
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #   - copy CORE/@"lower_plate":0
          "_value": [copy_value, 0],
        },
        {
          "_name": "lower_vfrac",
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #   - copy CORE/@"lower_plate":2
          "_value": [copy_value, 2],
        }
      ]
    },
    "upper_plate": {
      "_output": [
        {
          "_name": "upper_thick",
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #   - copy CORE/@"upper_plate":1
          "_value": [copy_value, 1],
        },
        {
          "_name": "upper_mat",
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #   - copy CORE/@"upper_plate":0
          "_value": [copy_value, 0],
        },
        {
          "_name": "upper_vfrac",
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #   - copy CORE/@"upper_plate":2
          "_value": [copy_value, 2],
        }
      ]
    },
    "bc_bot": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #   - copy CORE/$bc_bot
          "_value": copy_value,
        }
      ]
    },
    "bc_sym": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #   - copy CORE/$bc_sym
          "_value": copy_value,
        }
      ]
    },
    "bc_top": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #   - copy CORE/$bc_top
          "_value": copy_value,
        }
      ]
    },
    "bc_rad": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #   - copy CORE/$bc_rad
          "_value": copy_value,
        }
      ]
    },
    "xlabel": {
      "_output": [
        {
          "_pltype": "array",
          "_type": "string",
          # "_do":
          #   - copy CORE/@xlabel
          "_value": copy_array,
        }
      ]
    },
    "ylabel": {
      "_output": [
        {
          "_pltype": "array",
          "_type": "string",
          # "_do":
          #   - copy CORE/@ylabel
          "_value": copy_array,
        }
      ]
    },
    "label_format": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #   - copy CORE/@label_format
          "_value": copy_value,
        }
      ]
    },
    "height": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #   - copy CORE/$height
          "_value": copy_value,
        }
      ]
    },
    "upper_ref": {
      "_output": [
        {
          "_name": "upper_refl_mats",
          "_pltype": "array",
          "_type": "string",
          # "_do":
          #   - copyarray CORE/@upper_ref,start=>0,stride=>3
          "_value": [copy_value, slice(0, None, 3)],
        },
        {
          "_name": "upper_refl_thicks",
          "_pltype": "array",
          "_type": "double",
          # "_do":
          #   - copyarray CORE/@upper_ref,start=>1,stride=>3
          "_value": [copy_value, slice(1, None, 3)],
        },
        {
          "_name": "upper_refl_vfracs",
          "_pltype": "array",
          "_type": "double",
          # "_do":
          #   - copyarray CORE/@upper_ref,start=>2,stride=>3
          "_value": [copy_value, slice(2, None, 3)],
        }
      ]
    },
    "lower_ref": {
      "_output": [
        {
          "_name": "lower_refl_mats",
          "_pltype": "array",
          "_type": "string",
          # "_do":
          #   - copyarray CORE/@lower_ref,start=>0,stride=>3
          "_value": [copy_value, slice(0, None, 3)],
        },
        {
          "_name": "lower_refl_thicks",
          "_pltype": "array",
          "_type": "double",
          # "_do":
          #   - copyarray CORE/@lower_ref,start=>1,stride=>3
          "_value": [copy_value, slice(1, None, 3)],
        },
        {
          "_name": "lower_refl_vfracs",
          "_pltype": "array",
          "_type": "double",
          # "_do":
          #   - copyarray CORE/@lower_ref,start=>2,stride=>3
          "_value": [copy_value, slice(2, None, 3)],
        }
      ]
    },
    "Materials": {
      "_output": [
        {
          "_pltype": "list",
          # "_do":
          #   - matmap Material_,CORE/%mat/*
          "_value": copy_value,
        }
      ]
    },
    "reactor_type": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #   - copy CORE/$reactor_type
          "_value": copy_value,
        }
      ]
    },
    "Sources": {
      "_output": [
        {
          "_pltype": "list",
          # "_do":
          #   - sourcemap Source_,CORE/%source/*
          "_value": copy_value,
        }
      ]
    },
  }
}
