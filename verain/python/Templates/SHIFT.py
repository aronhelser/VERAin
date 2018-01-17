from __future__ import absolute_import, division, print_function

from Templates.Utils import *

SHIFT = {
  "_content": {
    "transport": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy SHIFT/$transport
          "_value": copy_value,
        }
      ]
    },
    "problem_mode": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy SHIFT/$problem_mode
          "_value": copy_value,
        }
      ]
    },
    "mode": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy SHIFT/$mode
          "_value": copy_value,
        }
      ]
    },
    "celib_file": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy SHIFT/$celib_file
          "_value": copy_value,
        }
      ]
    },
    "transfer": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy SHIFT/$transfer
          "_value": copy_value,
        }
      ]
    },
    "temp_transfer": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy SHIFT/$temp_transfer
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
          #  - copy SHIFT/$global_log
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
          #  - copy SHIFT/$local_log
          "_value": copy_value,
        }
      ]
    },
    "do_micro_tally": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "bool",
          # "_do":
          #  - copy SHIFT/$do_micro_tally
          "_value": copy_value,
        }
      ]
    },
    "output_geometry": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "bool",
          # "_do":
          #  - copy SHIFT/$output_geometry
          "_value": copy_value,
        }
      ]
    },
    "output_micro_tally": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "bool",
          # "_do":
          #  - copy SHIFT/$output_micro_tally
          "_value": copy_value,
        }
      ]
    },
    "output_fission_source": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "bool",
          # "_do":
          #  - copy SHIFT/$output_fission_source
          "_value": copy_value,
        }
      ]
    },
    "thermal_energy_cutoff": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy SHIFT/$thermal_energy_cutoff
          "_value": copy_value,
        }
      ]
    },
    "excore_filename": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy SHIFT/$excore_filename
          "_value": copy_value,
        }
      ]
    },
    "core_translate": {
      "_output": [
        {
          "_pltype": "array",
          "_type": "double",
          # "_do":
          #  - copyarray SHIFT/$core_translate
          "_value": copy_value,
        }
      ]
    },
    "create_unique_pins": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "bool",
          # "_do":
          #  - copy SHIFT/$create_unique_pins
          "_value": copy_value,
        }
      ]
    },
    "track_isotopes": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy SHIFT/$track_isotopes
          "_value": copy_value,
        }
      ]
    },
        "Np": {
          "_inlist": "kcode_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "double",
              # Special Case: duplicate this parameter outside the list, too.
              "_notInList": True,
              # "_do":
              #  - copy SHIFT/$Np
              "_value": copy_value,
            }
          ]
        },
        "num_cycles": {
          "_inlist": "kcode_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy SHIFT/$num_cycles
              "_value": copy_value,
            }
          ]
        },
        "num_inactive_cycles": {
          "_inlist": "kcode_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy SHIFT/$num_inactive_cycles
              "_value": copy_value,
            }
          ]
        },
    "dbrc": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "bool",
          # "_do":
          #  - copy SHIFT/$dbrc
          "_value": copy_value,
        }
      ]
    },
    "broaden_xs": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "bool",
          # "_do":
          #  - copy SHIFT/$broaden_xs
          "_value": copy_value,
        }
      ]
    },

        "temperature_tol": {
          "_inlist": "broaden_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "double",
              # "_do":
              #  - copy SHIFT/$temperature_tol
              "_value": copy_value,
            }
          ]
        },
        "union_energy": {
          "_inlist": "broaden_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "bool",
              # "_do":
              #  - copy SHIFT/$union_energy
              "_value": copy_value,
            }
          ]
        },
        "delta_t": {
          "_inlist": "broaden_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "double",
              # "_do":
              #  - copy SHIFT/$delta_t
              "_value": copy_value,
            }
          ]
        },
        "energy_tol": {
          "_inlist": "broaden_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "double",
              # "_do":
              #  - copy SHIFT/$energy_tol
              "_value": copy_value,
            }
          ]
        },

        "radial_mesh": {
          "_inlist": "tally_db",
          "_output": [
            {
              "_pltype": "array",
              "_type": "double",
              # "_do":
              #  - copyarray SHIFT/$radial_mesh
              "_value": copy_value,
            }
          ]
        },
        "num_theta": {
          "_inlist": "tally_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy SHIFT/$num_theta
              "_value": copy_value,
            }
          ]
        },
        "num_axial": {
          "_inlist": "tally_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy SHIFT/$num_axial
              "_value": copy_value,
            }
          ]
        },
        "n_bounds": {
          "_inlist": "tally_db",
          "_output": [
            {
              "_pltype": "array",
              "_type": "double",
              # "_do":
              #  - copyarray SHIFT/$n_bounds
              "_value": copy_value,
            }
          ]
        },
        "p_bounds": {
          "_inlist": "tally_db",
          "_output": [
            {
              "_pltype": "array",
              "_type": "double",
              # "_do":
              #  - copyarray SHIFT/$p_bounds
              "_value": copy_value,
            }
          ]
        },
        "micro_zaids": {
          "_inlist": "tally_db",
          "_output": [
            {
              "_pltype": "array",
              "_type": "int",
              # "_do":
              #  - copyarray SHIFT/$micro_zaids
              "_value": copy_value,
            }
          ]
        },
        "micro_rxns": {
          "_inlist": "tally_db",
          "_output": [
            {
              "_pltype": "array",
              "_type": "int",
              # "_do":
              #  - copyarray SHIFT/$micro_rxns
              "_value": copy_value,
            }
          ]
        },
        "gamma_flux": {
          "_inlist": "tally_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "bool",
              # "_do":
              #  - copy SHIFT/$gamma_flux
              "_value": copy_value,
            }
          ]
        },

        "bc_bnd_mesh": {
          "_inlist": "boundary_mesh_db",
          "_output": [
            {
              "_pltype": "array",
              "_type": "string",
              # "_do":
              #  - copyarray SHIFT/$bc_bnd_mesh
              "_value": copy_value,
            }
          ]
        },
        "x_bnd_mesh": {
          "_inlist": "boundary_mesh_db",
          "_output": [
            {
              "_pltype": "array",
              "_type": "double",
              # "_do":
              #  - copyarray SHIFT/$x_bnd_mesh
              "_value": copy_value,
            }
          ]
        },
        "y_bnd_mesh": {
          "_inlist": "boundary_mesh_db",
          "_output": [
            {
              "_pltype": "array",
              "_type": "double",
              # "_do":
              #  - copy SHIFT/$y_bnd_mesh
              "_value": copy_value,
            }
          ]
        },
        "z_bnd_mesh": {
          "_inlist": "boundary_mesh_db",
          "_output": [
            {
              "_pltype": "array",
              "_type": "double",
              # "_do":
              #  - copy SHIFT/$z_bnd_mesh
              "_value": copy_value,
            }
          ]
        },

        "problem_name": {
          "_inlist": "hybrid_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy SHIFT/$problem_name
              "_value": copy_value,
            }
          ]
        },
        "xs_library": {
          "_inlist": "hybrid_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy SHIFT/$xs_library
              "_value": copy_value,
            }
          ]
        },
        "mesh": {
          "_inlist": "hybrid_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # Special Case: duplicate this parameter outside the list, too.
              "_notInList": True,
              # "_do":
              #  - copy SHIFT/$mesh
              "_value": copy_value,
            }
          ]
        },
        "dimension": {
          "_inlist": "hybrid_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy SHIFT/$dimension
              "_value": copy_value,
            }
          ]
        },
        "do_transport": {
          "_inlist": "hybrid_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "bool",
              # Special Case: duplicate this parameter outside the list, too.
              "_notInList": True,
              # "_do":
              #  - copy SHIFT/$do_transport
              "_value": copy_value,
            }
          ]
        },
        "do_output": {
          "_inlist": "hybrid_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "bool",
              # Special Case: duplicate this parameter outside the list, too.
              "_notInList": True,
              # "_do":
              #  - copy SHIFT/$do_output
              "_value": copy_value,
            }
          ]
        },
        "output_adjoint": {
          "_inlist": "hybrid_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "bool",
              # "_do":
              #  - copy SHIFT/$output_adjoint
              "_value": copy_value,
            }
          ]
        },
        "adjoint": {
          "_inlist": "hybrid_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "bool",
              # "_do":
              #  - copy SHIFT/$adjoint
              "_value": copy_value,
            }
          ]
        },
        "num_blocks_i": {
          "_inlist": "hybrid_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy SHIFT/$num_blocks_i
              "_value": copy_value,
            }
          ]
        },
        "num_blocks_j": {
          "_inlist": "hybrid_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy SHIFT/$num_blocks_j
              "_value": copy_value,
            }
          ]
        },
        "num_z_blocks": {
          "_inlist": "hybrid_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy SHIFT/$num_z_blocks
              "_value": copy_value,
            }
          ]
        },
        "num_sets": {
          "_inlist": "hybrid_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy SHIFT/$num_sets
              "_value": copy_value,
            }
          ]
        },
        "num_groups": {
          "_inlist": "hybrid_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy SHIFT/$num_groups
              "_value": copy_value,
            }
          ]
        },
        "max_delta_z": {
          "_inlist": "hybrid_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "double",
              # "_do":
              #  - copy SHIFT/$max_delta_z
              "_value": copy_value,
            }
          ]
        },
        "store_fulcrum_string": {
          "_inlist": "hybrid_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "bool",
              # "_do":
              #  - copy SHIFT/$store_fulcrum_string
              "_value": copy_value,
            }
          ]
        },
        "downscatter": {
          "_inlist": "hybrid_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "bool",
              # "_do":
              #  - copy SHIFT/$downscatter
              "_value": copy_value,
            }
          ]
        },
        "Pn_order": {
          "_inlist": "hybrid_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy SHIFT/$Pn_order
              "_value": copy_value,
            }
          ]
        },
        "eq_set": {
          "_inlist": "hybrid_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy SHIFT/$eq_set
              "_value": copy_value,
            }
          ]
        },
        "new_grp_bounds": {
          "_inlist": "hybrid_db",
          "_output": [
            {
              "_pltype": "array",
              "_type": "double",
              # "_do":
              #  - copyarray SHIFT/$new_grp_bounds
              "_value": copy_value,
            }
          ]
        },
        "grp_collapse_src": {
          "_inlist": "hybrid_db",
          "_output": [
            {
              "_pltype": "array",
              "_type": "double",
              # "_do":
              #  - copyarray SHIFT/$grp_collapse_src
              "_value": copy_value,
            }
          ]
        },
        "cell_homogenize": {
          "_inlist": "hybrid_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "bool",
              # "_do":
              #  - copy SHIFT/$cell_homogenize
              "_value": copy_value,
            }
          ]
        },
        "SPN_matrix_type": {
          "_inlist": "hybrid_db",
          "_output": [
            {
              "_name": "spn_matrix_type",
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy SHIFT/$SPN_matrix_type
              "_value": copy_value,
            }
          ]
        },
        "SPN_order": {
          "_inlist": "hybrid_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy SHIFT/$SPN_order
              "_value": copy_value,
            }
          ]
        },

            "quad_type": {
              "_inlist": "hybrid_db,quadrature_db",
              "_output": [
                {
                  "_pltype": "parameter",
                  "_type": "string",
                  # "_do":
                  #  - copy SHIFT/$quad_type
                  "_value": copy_value,
                }
              ]
            },
            "polars_octant": {
              "_inlist": "hybrid_db,quadrature_db",
              "_output": [
                {
                  "_pltype": "parameter",
                  "_type": "int",
                  # "_do":
                  #  - copy SHIFT/$polars_octant
                  "_value": copy_value,
                }
              ]
            },
            "azimuthals_octant": {
              "_inlist": "hybrid_db,quadrature_db",
              "_output": [
                {
                  "_pltype": "parameter",
                  "_type": "int",
                  # "_do":
                  #  - copy SHIFT/$azimuthals_octant
                  "_value": copy_value,
                }
              ]
            },
            "Sn_order": {
              "_inlist": "hybrid_db,quadrature_db",
              "_output": [
                {
                  "_pltype": "parameter",
                  "_type": "int",
                  # "_do":
                  #  - copy SHIFT/$Sn_order
                  "_value": copy_value,
                }
              ]
            },

            "solver": {
              "_inlist": "hybrid_db,solver_db",
              "_output": [
                {
                  "_pltype": "parameter",
                  "_type": "string",
                  # "_do":
                  #  - copy SHIFT/$solver
                  "_value": copy_value,
                }
              ]
            },
            "tolerance": {
              "_inlist": "hybrid_db,solver_db",
              "_output": [
                {
                  "_pltype": "parameter",
                  "_type": "double",
                  # "_do":
                  #  - copy SHIFT/$tolerance
                  "_value": copy_value,
                }
              ]
            },
            "k_tolerance": {
              "_inlist": "hybrid_db,solver_db",
              "_output": [
                {
                  "_pltype": "parameter",
                  "_type": "double",
                  # "_do":
                  #  - copy SHIFT/$k_tolerance
                  "_value": copy_value,
                }
              ]
            },
            "subspace_size": {
              "_inlist": "hybrid_db,solver_db",
              "_output": [
                {
                  "_pltype": "parameter",
                  "_type": "int",
                  # "_do":
                  #  - copy SHIFT/$subspace_size
                  "_value": copy_value,
                }
              ]
            },
            "max_itr": {
              "_inlist": "hybrid_db,solver_db",
              "_output": [
                {
                  "_pltype": "parameter",
                  "_type": "int",
                  # "_do":
                  #  - copy SHIFT/$max_itr
                  "_value": copy_value,
                }
              ]
            },
            "verbosity": {
              "_inlist": "hybrid_db,solver_db",
              "_output": [
                {
                  "_pltype": "parameter",
                  "_type": "string",
                  # "_do":
                  #  - copy SHIFT/$verbosity
                  "_value": copy_value,
                }
              ]
            },
            "energy_dep_ev": {
              "_inlist": "hybrid_db,solver_db",
              "_output": [
                {
                  "_pltype": "parameter",
                  "_type": "bool",
                  # "_do":
                  #  - copy SHIFT/$energy_dep_ev
                  "_value": copy_value,
                }
              ]
            },
            "partition_upscatter": {
              "_inlist": "hybrid_db,solver_db",
              "_output": [
                {
                  "_pltype": "parameter",
                  "_type": "bool",
                  # "_do":
                  #  - copy SHIFT/$partition_upscatter
                  "_value": copy_value,
                }
              ]
            },

                "upscatter_tolerance": {
                  "_inlist": "hybrid_db,solver_db,upscatter_db",
                  "_output": [
                    {
                      "_name": "tolerance",
                      "_pltype": "parameter",
                      "_type": "double",
                      # "_do":
                      #  - copy SHIFT/$upscatter_tolerance
                      "_value": copy_value,
                    }
                  ]
                },
                "upscatter_solver": {
                  "_inlist": "hybrid_db,solver_db,upscatter_db",
                  "_output": [
                    {
                      "_name": "solver",
                      "_pltype": "parameter",
                      "_type": "string",
                      # "_do":
                      #  - copy SHIFT/$upscatter_solver
                      "_value": copy_value,
                    }
                  ]
                },
                "upscatter_max_itr": {
                  "_inlist": "hybrid_db,solver_db,upscatter_db",
                  "_output": [
                    {
                      "_name": "max_itr",
                      "_pltype": "parameter",
                      "_type": "int",
                      # "_do":
                      #  - copy SHIFT/$upscatter_max_itr
                      "_value": copy_value,
                    }
                  ]
                },
                "upscatter_subspace_size": {
                  "_inlist": "hybrid_db,solver_db,upscatter_db",
                  "_output": [
                    {
                      "_name": "subspace_size",
                      "_pltype": "parameter",
                      "_type": "int",
                      # "_do":
                      #  - copy SHIFT/$upscatter_subspace_size
                      "_value": copy_value,
                    }
                  ]
                },
                "upscatter_verbosity": {
                  "_inlist": "hybrid_db,solver_db,upscatter_db",
                  "_output": [
                    {
                      "_name": "verbosity",
                      "_pltype": "parameter",
                      "_type": "string",
                      # "_do":
                      #  - copy SHIFT/$upscatter_verbosity
                      "_value": copy_value,
                    }
                  ]
                },
                "iterate_downscatter": {
                  "_inlist": "hybrid_db,solver_db,upscatter_db",
                  "_output": [
                    {
                      "_pltype": "parameter",
                      "_type": "bool",
                      # "_do":
                      #  - copy SHIFT/$iterate_downscatter
                      "_value": copy_value,
                    }
                  ]
                },
        "Pn_correction": {
          "_inlist": "hybrid_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "bool",
              # "_do":
              #  - copy SHIFT/$Pn_correction
              "_value": copy_value,
            }
          ]
        },
        "pin_partitioning": {
          "_inlist": "hybrid_db",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "bool",
              # "_do":
              #  - copy SHIFT/$pin_partitioning
              "_value": copy_value,
            }
          ]
        },
  }
}
