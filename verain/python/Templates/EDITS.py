from __future__ import absolute_import, division, print_function

from Templates.Utils import *

EDITS = {
  "_pltype": "list",
  "_content": {
    "axial_edit_bounds": {
      "_output": [
        {
          "_pltype": "array",
          "_type": "double",
          # "_do":
          #  - copy EDITS/@axial_edit_bounds
          "_value": copy_array,
        }
      ]
    },
    "axial_edit_mesh_delta": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy EDITS/$axial_edit_mesh_delta
          "_value": copy_value,
        }
      ]
    },
    "points": {
      "_output": [
        {
          "_name": "points_type",
          "_pltype": "array",
          "_type": "string",
          # "_do":
          #  - copyarray EDITS/@points,start=>0,stride=>4
          "_value": [copy_array, slice(0, None, 4)],
        },
        {
          "_name": "points_dim1",
          "_pltype": "array",
          "_type": "double",
          # "_do":
          #  - copyarray EDITS/@points,start=>1,stride=>4
          "_value": [copy_array, slice(1, None, 4)],
        },
        {
          "_name": "points_dim2",
          "_pltype": "array",
          "_type": "double",
          # "_do":
          #  - copyarray EDITS/@points,start=>2,stride=>4
          "_value": [copy_array, slice(2, None, 4)],
        },
        {
          "_name": "points_dim3",
          "_pltype": "array",
          "_type": "double",
          # "_do":
          #  - copyarray EDITS/@points,start=>3,stride=>4
          "_value": [copy_array, slice(3, None, 4)],
        }
      ]
    },
    "edit_group": {
      "_pltype": "list",
      "_name": "edit_group",
      "_listName": "%s",
      "_output": [
        {
          "_name": "edit_group_name",
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - value (_loop)
          "_value": [copy_value, 0],
        },
        {
          "_name": "edit_vars",
          "_pltype": "array",
          "_type": "string",
          # "_do":
          #  - copyarray EDITS/%edit_group/$(_loop)
          "_value": [copy_array, slice(1, None)],
        },
      ]
    }
  }
}
