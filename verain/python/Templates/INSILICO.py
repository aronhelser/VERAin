from __future__ import absolute_import, division, print_function

from Templates.Utils import *

INSILICO = {
  "_content": {
    "problem_name": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy INSILICO/$problem_name
          "_value": copy_value,
        }
      ]
    },
    "xs_library": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy INSILICO/$xs_library
          "_value": copy_value,
        }
      ]
    },
    "temp_correction": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy INSILICO/$temp_correction
          "_value": copy_value,
        }
      ]
    },
    "global_log": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy INSILICO/$global_log
          "_value": copy_value,
        }
      ]
    },
    "local_log": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy INSILICO/$local_log
          "_value": copy_value,
        }
      ]
    },
    "mesh": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "int",
          # "_do":
          #  - copy INSILICO/$mesh
          "_value": copy_value,
        }
      ]
    },
    "dimension": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "int",
          # "_do":
          #  - copy INSILICO/$dimension
          "_value": copy_value,
        }
      ]
    },
    "use_symmetry": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "bool",
          # "_do":
          #  - copy INSILICO/$use_symmetry
          "_value": copy_value,
        }
      ]
    },
    "do_transport": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "bool",
          # "_do":
          #  - copy INSILICO/$do_transport
          "_value": copy_value,
        }
      ]
    },
    "do_output": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "bool",
          # "_do":
          #  - copy INSILICO/$do_output
          "_value": copy_value,
        }
      ]
    },
    "geometry_output": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "bool",
          # "_do":
          #  - copy INSILICO/$geometry_output
          "_value": copy_value,
        }
      ]
    },
    "num_blocks_i": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "int",
          # "_do":
          #  - copy INSILICO/$num_blocks_i
          "_value": copy_value,
        }
      ]
    },
    "num_blocks_j": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "int",
          # "_do":
          #  - copy INSILICO/$num_blocks_j
          "_value": copy_value,
        }
      ]
    },
    "num_z_blocks": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "int",
          # "_do":
          #  - copy INSILICO/$num_z_blocks
          "_value": copy_value,
        }
      ]
    },
    "num_sets": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "int",
          # "_do":
          #  - copy INSILICO/$num_sets
          "_value": copy_value,
        }
      ]
    },
    "num_groups": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "int",
          # "_do":
          #  - copy INSILICO/$num_groups
          "_value": copy_value,
        }
      ]
    },
    "radial_geom_eps": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy INSILICO/$radial_geom_eps
          "_value": copy_value,
        }
      ]
    },
    "axial_geom_eps": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy INSILICO/$axial_geom_eps
          "_value": copy_value,
        }
      ]
    },
    "max_delta_z": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy INSILICO/$max_delta_z
          "_value": copy_value,
        }
      ]
    },
    "store_fulcrum_string": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy INSILICO/$store_fulcrum_string
          "_value": copy_value,
        }
      ]
    },
    "downscatter": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy INSILICO/$downscatter
          "_value": copy_value,
        }
      ]
    },
    "Pn_order": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "int",
          # "_do":
          #  - copy INSILICO/$Pn_order
          "_value": copy_value,
        }
      ]
    },
    "cell_broadcast_size": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "int",
          # "_do":
          #  - copy INSILICO/$cell_broadcast_size
          "_value": copy_value,
        }
      ]
    },
    "eq_set": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy INSILICO/$eq_set
          "_value": copy_value,
        }
      ]
    },
    "new_grp_bounds": {
      "_output": [
        {
          "_pltype": "array",
          "_type": "double",
          # "_do":
          #  - copyarray INSILICO/@new_grp_bounds
          "_value": copy_array,
        }
      ]
    },
    "cell_homogenize": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "bool",
          # "_do":
          #  - copy INSILICO/$cell_homogenize
          "_value": copy_value,
        }
      ]
    },
    "SPN_matrix_type": {
      "_output": [
        {
          "_name": "spn_matrix_type",
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy INSILICO/$SPN_matrix_type
          "_value": copy_value,
        }
      ]
    },
    "SPN_order": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "int",
          # "_do":
          #  - copy INSILICO/$SPN_order
          "_value": copy_value,
        }
      ]
    },
    "quadrature_db": {
      "_output": [
        {
          "_pltype": "list",
          "_value": copy_value,
        }
      ]
    },
        "quad_type": {
          "_inlist": "quadrature_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy INSILICO/$quad_type
              "_value": copy_value,
            }
          ]
        },
        "polars_octant": {
          "_inlist": "quadrature_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy INSILICO/$polars_octant
              "_value": copy_value,
            }
          ]
        },
        "azimuthals_octant": {
          "_inlist": "quadrature_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy INSILICO/$azimuthals_octant
              "_value": copy_value,
            }
          ]
        },
        "Sn_order": {
          "_inlist": "quadrature_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy INSILICO/$Sn_order
              "_value": copy_value,
            }
          ]
        },

        "solver": {
          "_inlist": "solver_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy INSILICO/$solver
              "_value": copy_value,
            }
          ]
        },
        "tolerance": {
          "_inlist": "solver_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "double",
              # "_do":
              #  - copy INSILICO/$tolerance
              "_value": copy_value,
            }
          ]
        },
        "k_tolerance": {
          "_inlist": "solver_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "double",
              # "_do":
              #  - copy INSILICO/$k_tolerance
              "_value": copy_value,
            }
          ]
        },
        "subspace_size": {
          "_inlist": "solver_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy INSILICO/$subspace_size
              "_value": copy_value,
            }
          ]
        },
        "max_itr": {
          "_inlist": "solver_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy INSILICO/$max_itr
              "_value": copy_value,
            }
          ]
        },
        "verbosity": {
          "_inlist": "solver_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy INSILICO/$verbosity
              "_value": copy_value,
            }
          ]
        },
        "energy_dep_ev": {
          "_inlist": "solver_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "bool",
              # "_do":
              #  - copy INSILICO/$energy_dep_ev
              "_value": copy_value,
            }
          ]
        },
        "partition_upscatter": {
          "_inlist": "solver_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "bool",
              # "_do":
              #  - copy INSILICO/$partition_upscatter
              "_value": copy_value,
            }
          ]
        },

            "upscatter_tolerance": {
              "_inlist": "solver_db,upscatter_db",
              "_output": [
                {
                  "_name": "tolerance",
                  "_pltype": "parameter",
                  "_type": "double",
                  # "_do":
                  #  - copy INSILICO/$upscatter_tolerance
                  "_value": copy_value,
                }
              ]
            },
            "upscatter_solver": {
              "_inlist": "solver_db,upscatter_db",
              "_output": [
                {
                  "_name": "solver",
                  "_pltype": "parameter",
                  "_type": "string",
                  # "_do":
                  #  - copy INSILICO/$upscatter_solver
                  "_value": copy_value,
                }
              ]
            },
            "upscatter_max_itr": {
              "_inlist": "solver_db,upscatter_db",
              "_output": [
                {
                  "_name": "max_itr",
                  "_pltype": "parameter",
                  "_type": "int",
                  # "_do":
                  #  - copy INSILICO/$upscatter_max_itr
                  "_value": copy_value,
                }
              ]
            },
            "upscatter_verbosity": {
              "_inlist": "solver_db,upscatter_db",
              "_output": [
                {
                  "_name": "verbosity",
                  "_pltype": "parameter",
                  "_type": "string",
                  # "_do":
                  #  - copy INSILICO/$upscatter_verbosity
                  "_value": copy_value,
                }
              ]
            },
            "iterate_downscatter": {
              "_inlist": "solver_db,upscatter_db",
              "_output": [
                {
                  "_pltype": "parameter",
                  "_type": "bool",
                  # "_do":
                  #  - copy INSILICO/$iterate_downscatter
                  "_value": copy_value,
                }
              ]
            },

        "silo_output": {
          "_inlist": "silo_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy INSILICO/$silo_output
              "_value": copy_value,
            }
          ]
        },
        "mixing_table": {
          "_inlist": "silo_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "bool",
              # "_do":
              #  - copy INSILICO/$mixing_table
              "_value": copy_value,
            }
          ]
        },
    "Pn_correction": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "bool",
          # "_do":
          #  - copy INSILICO/$Pn_correction
          "_value": copy_value,
        }
      ]
    },
    "pin_partitioning": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "bool",
          # "_do":
          #  - copy INSILICO/$pin_partitioning
          "_value": copy_value,
        }
      ]
    },
  }
}
