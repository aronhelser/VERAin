from __future__ import absolute_import, division, print_function

from Templates.Utils import *

MPACT = {
  "_content": {
    "include": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # TODO include file contents
          "_value": copy_value,
        }
      ]
    },
    "ray_spacing": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy MPACT/$ray_spacing
          "_value": copy_value,
        }
      ]
    },
    "shield_ray_spacing": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy MPACT/$shield_ray_spacing
          "_value": copy_value,
        }
      ]
    },
    "log_message": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy MPACT/$log_message
          "_value": copy_value,
        }
      ]
    },
    "refl_no_added_modules": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy MPACT/$refl_no_added_modules
          "_value": copy_value,
        }
      ]
    },
    "refl_highres": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy MPACT/$refl_highres
          "_value": copy_value,
        }
      ]
    },
    "moc_kernel": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy MPACT/$moc_kernel
          "_value": copy_value,
        }
      ]
    },
    "moc_mg_data_passing": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "bool",
          # "_do":
          #  - copy MPACT/$moc_mg_data_passing
          "_value": copy_value,
        }
      ]
    },
    "shield_moc_kernel": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy MPACT/$shield_moc_kernel
          "_value": copy_value,
        }
      ]
    },
    "volume_corr": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy MPACT/$volume_corr
          "_value": copy_value,
        }
      ]
    },
    "modular_rays": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy MPACT/$modular_rays
          "_value": copy_value,
        }
      ]
    },
    "power_edit": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy MPACT/$power_edit
          "_value": copy_value,
        }
      ]
    },
    "valid_on": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "bool",
          # "_do":
          #  - copy MPACT/$valid_on
          "_value": copy_value,
        }
      ]
    },
    "valid_delim": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy MPACT/$valid_delim
          "_value": copy_value,
        }
      ]
    },
    "checkpoint_mode": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy MPACT/$checkpoint_mode
          "_value": copy_value,
        }
      ]
    },
    "checkpoint_file": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy MPACT/$checkpoint_file
          "_value": copy_value,
        }
      ]
    },
    "vis_edits": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy MPACT/$vis_edits
          "_value": copy_value,
        }
      ]
    },
    "rr_edits": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy MPACT/$rr_edits
          "_value": copy_value,
        }
      ]
    },
    "rr_edits_opt": {
      "_output": [
        {
          "_pltype": "array",
          "_type": "string",
          # "_do":
          #  - copy MPACT/$rr_edits_opt
          "_value": copy_value,
        }
      ]
    },
    "rod_treatment": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy MPACT/$rod_treatment
          "_value": copy_value,
        }
      ]
    },
    "ppm_method": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy MPACT/$ppm_method
          "_value": copy_value,
        }
      ]
    },
    "jagged": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "bool",
          # "_do":
          #  - copy MPACT/$jagged
          "_value": copy_value,
        }
      ]
    },
    "grid_treatment": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy MPACT/$grid_treatment
          "_value": copy_value,
        }
      ]
    },
    "axial_buckling": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy MPACT/$axial_buckling
          "_value": copy_value,
        }
      ]
    },
    "mat_emit_src": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "bool",
          # "_do":
          #  - copy MPACT/$mat_emit_src
          "_value": copy_value,
        }
      ]
    },
    "uniform_crud": {
      "_output": [
        {
          "_pltype": "list",
          "_value": copy_value,
        }
      ]
    },
        "crud_thickness": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "double",
              # "_do":
              #  - copy MPACT/@"uniform_crud":0
              "_value": copy_value,
            }
          ]
        },
        "crud_mass": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "double",
              # "_do":
              #  - copy MPACT/@"uniform_crud":1
              "_value": copy_value,
            }
          ]
        },
        "boron_mass": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "double",
              # "_do":
              #  - copy MPACT/@"uniform_crud":2
              "_value": copy_value,
            }
          ]
        },
    "crud_depletion": {
      "_output": [
        {
          "_pltype": "list",
          "_value": copy_value,
        }
      ]
    },        "flag": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "bool",
              # "_do":
              #  - copy MPACT/@"crud_depletion":0
              "_value": copy_value,
            }
          ]
        },
        "crud_depfrac": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "double",
              # "_do":
              #  - copy MPACT/@"crud_depletion":1
              "_value": copy_value,
            }
          ]
        },
    "db_entry": {
      "_output": [
        {
          "_pltype": "list",
          # "_do":
          #  - mpact_db db_entry_,MPACT/%db_entry/*
          "_value": copy_value,
        }
      ]
    },
    "quad_set": {
      "_output": [
        {
          "_pltype": "list",
          "_value": copy_value,
        }
      ]
    },        "quad_type": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy MPACT/$quad_type
              "_value": copy_value,
            }
          ]
        },
        "shield_quad_type": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy MPACT/$shield_quad_type
              "_value": copy_value,
            }
          ]
        },
        "polars_octant": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy MPACT/$polars_octant
              "_value": copy_value,
            }
          ]
        },
        "azimuthals_octant": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy MPACT/$azimuthals_octant
              "_value": copy_value,
            }
          ]
        },
        "shield_azimuthals_octant": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy MPACT/$shield_azimuthals_octant
              "_value": copy_value,
            }
          ]
        },
        "shield_polars_octant": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy MPACT/$shield_polars_octant
              "_value": copy_value,
            }
          ]
        },
    "mesh": {
      "_pltype": "list",
      "_name": "pinmesh",
      "_listName": "pinmesh_%s",
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
          "_name": "num_rad",
          "_pltype": "array",
          "_type": "int",
          # have to skip the label
          "_value": [copy_array_before_val, '/', slice(1, None)],
        },
        {
          "_name": "num_theta",
          "_pltype": "array",
          "_type": "int",
          "_value": [copy_array_after_val, '/'],
        },
      ]
    },
        "automesh_bounds_min": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "double",
              # "_do":
              #  - copy MPACT/$"automesh_bounds":0
              "_value": copy_value,
            }
          ]
        },
        "automesh_bounds_max": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "double",
              # "_do":
              #  - copy MPACT/$"automesh_bounds":1
              "_value": copy_value,
            }
          ]
        },
        "meshing_method": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy MPACT/$meshing_method
              "_value": copy_value,
            }
          ]
        },
        "axial_mesh": {
          "_output": [
            {
              "_pltype": "array",
              "_type": "double",
              # "_do":
              #  - copy MPACT/$axial_mesh
              "_value": copy_value,
            }
          ]
        },
        "crud_mesh_thickness": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "double",
              # "_do":
              #  - copy MPACT/@"crud_mesh":0
              "_value": copy_value,
            }
          ]
        },
        "crud_mesh_div": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy MPACT/@"crud_mesh":1
              "_value": copy_value,
            }
          ]
        },
        "moderator_mesh_ndiv": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy MPACT/@"pin_cell_mod_mesh":0
              "_value": copy_value,
            }
          ]
        },
        "moderator_mesh_pins": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy MPACT/@"pin_cell_mod_mesh":1
              "_value": copy_value,
            }
          ]
        },
    "parallel_env": {
      "_output": [
        {
          "_pltype": "list",
          "_value": copy_value,
        }
      ]
    },
        "num_space": {
          "_inlist": "parallel_env",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy MPACT/$num_space
              "_value": copy_value,
            }
          ]
        },
        "num_angle": {
          "_inlist": "parallel_env",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy MPACT/$num_angle
              "_value": copy_value,
            }
          ]
        },
        "num_energy": {
          "_inlist": "parallel_env",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy MPACT/$num_energy
              "_value": copy_value,
            }
          ]
        },
        "num_threads": {
          "_inlist": "parallel_env",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy MPACT/$num_threads
              "_value": copy_value,
            }
          ]
        },
        "par_method": {
          "_inlist": "parallel_env",
          "_output": [
            {
              "_name": "method",
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy MPACT/$par_method
              "_value": copy_value,
            }
          ]
        },
        "par_file": {
          "_inlist": "parallel_env",
          "_output": [
            {
              "_name": "filename",
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy MPACT/$par_file
              "_value": copy_value,
            }
          ]
        },
        "par_xdim": {
          "_inlist": "parallel_env",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy MPACT/$par_xdim
              "_value": copy_value,
            }
          ]
        },
        "par_ydim": {
          "_inlist": "parallel_env",
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy MPACT/$par_ydim
              "_value": copy_value,
            }
          ]
        },
        "par_map": {
          "_inlist": "parallel_env",
          "_output": [
            {
              "_pltype": "array",
              "_type": "int",
              # "_do":
              #  - copyarray MPACT/@par_map
              "_value": copy_array,
            }
          ]
        },
        "graph": {
          "_output": [
            {
              "_pltype": "list",
              "_value": copy_value,
            }
          ]
        },
            "decomposition": {
              "_output": [
                {
                  "_pltype": "array",
                  "_type": "string",
                  # "_do":
                  #  - copyarray MPACT/@graph_part_method
                  "_value": copy_value,
                }
              ]
            },
            "refinement": {
              "_output": [
                {
                  "_pltype": "array",
                  "_type": "string",
                  # "_do":
                  #  - copyarray MPACT/@graph_refn_method
                  "_value": copy_value,
                }
              ]
            },
            "conditions": {
              "_output": [
                {
                  "_pltype": "array",
                  "_type": "int",
                  # "_do":
                  #  - copyarray MPACT/@graph_cond
                  "_value": copy_value,
                }
              ]
            },
    "iteration_control": {
      "_output": [
        {
          "_pltype": "list",
          "_value": copy_value,
        }
      ]
    },
        "k_tolerance": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "double",
              # "_do":
              #  - copy MPACT/$k_tolerance
              "_value": copy_value,
            }
          ]
        },
        "flux_tolerance": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "double",
              # "_do":
              #  - copy MPACT/$flux_tolerance
              "_value": copy_value,
            }
          ]
        },
        "num_outers": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy MPACT/$num_outers
              "_value": copy_value,
            }
          ]
        },
        "num_inners": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy MPACT/$num_inners
              "_value": copy_value,
            }
          ]
        },
        "up_scatter": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy MPACT/$up_scatter
              "_value": copy_value,
            }
          ]
        },
        "num_extsrc_itrs": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy MPACT/$num_extsrc_itrs
              "_value": copy_value,
            }
          ]
        },
        "scattering": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy MPACT/$scattering
              "_value": copy_value,
            }
          ]
        },
        "trim_Pn_moments": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "bool",
              # "_do":
              #  - copy MPACT/$trim_Pn_moments
              "_value": copy_value,
            }
          ]
        },
        "boundary_update": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy MPACT/$boundary_update
              "_value": copy_value,
            }
          ]
        },
    "depletion": {
      "_output": [
        {
          "_pltype": "list",
          "_value": copy_value,
        }
      ]
    },
        "dep_filename": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy MPACT/$dep_filename
              "_value": copy_value,
            }
          ]
        },
        "dep_edit": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy MPACT/$dep_edit
              "_value": copy_value,
            }
          ]
        },
        "dep_substep": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy MPACT/$dep_substep
              "_value": copy_value,
            }
          ]
        },
        "dep_kernel": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy MPACT/$dep_kernel
              "_value": copy_value,
            }
          ]
        },
        "depl_time_method": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy MPACT/$depl_time_method
              "_value": copy_value,
            }
          ]
        },
        "include_depl_mats": {
          "_output": [
            {
              "_pltype": "array",
              "_type": "string",
              # "_do":
              #  - copy MPACT/$include_depl_mats
              "_value": copy_value,
            }
          ]
        },
        "exclude_depl_mats": {
          "_output": [
            {
              "_pltype": "array",
              "_type": "string",
              # "_do":
              #  - copy MPACT/$exclude_depl_mats
              "_value": copy_value,
            }
          ]
        },    "TH": {
      "_output": [
        {
          "_pltype": "list",
          "_value": copy_value,
        }
      ]
    },
        "coupling_method": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy MPACT/$coupling_method
              "_value": copy_value,
            }
          ]
        },
        "nonlinear_solver": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy MPACT/$th_nonlinear_solver
              "_value": copy_value,
            }
          ]
        },
        "average_ftemp": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "bool",
              # "_do":
              #  - copy MPACT/$average_ftemp
              "_value": copy_value,
            }
          ]
        },
        "shield_max_outers": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy MPACT/$"shielder_th":0
              "_value": copy_value,
            }
          ]
        },
        "shield_min_dT": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "double",
              # "_do":
              #  - copy MPACT/$"shielder_th":1
              "_value": copy_value,
            }
          ]
        },
        "shield_min_drho": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "double",
              # "_do":
              #  - copy MPACT/$"shielder_th":2
              "_value": copy_value,
            }
          ]
        },
        "outers_per_TH": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy MPACT/$outers_per_TH
              "_value": copy_value,
            }
          ]
        },
        "depthAnderson": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy MPACT/$"anderson_options":0
              "_value": copy_value,
            }
          ]
        },
        "mixAnderson": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "double",
              # "_do":
              #  - copy MPACT/$"anderson_options":1
              "_value": copy_value,
            }
          ]
        },
        "startAnderson": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy MPACT/$"anderson_options":2
              "_value": copy_value,
            }
          ]
        },
        "ctf_basename": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy MPACT/$ctf_basename
              "_value": copy_value,
            }
          ]
        },
        "sth_dhfrac": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "double",
              # "_do":
              #  - copy MPACT/$sth_dhfrac
              "_value": copy_value,
            }
          ]
        },
        "sth_hgap": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "double",
              # "_do":
              #  - copy MPACT/$sth_hgap
              "_value": copy_value,
            }
          ]
        },
        "sth_channeltype": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy MPACT/$sth_channeltype
              "_value": copy_value,
            }
          ]
        },
        "sth_tabletype": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy MPACT/$sth_tabletype
              "_value": copy_value,
            }
          ]
        },
        "sth_avgpin": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "bool",
              # "_do":
              #  - copy MPACT/$sth_avgpin
              "_value": copy_value,
            }
          ]
        },
        "temptable_shape": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "bool",
              # "_do":
              #  - copy MPACT/$temptable_shape
              "_value": copy_value,
            }
          ]
        },
        "temptable_filename": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy MPACT/$temptable_filename
              "_value": copy_value,
            }
          ]
        },
        "temptable": {
          "_output": [
            {
              "_pltype": "list",
              "_value": copy_value,
            }
          ]
        },
            "qprime": {
              "_output": [
                {
                  "_pltype": "parameter",
                  "_type": "double",
                  # "_do":
                  #  - copy MPACT/$temptable_qprime
                  "_value": copy_value,
                }
              ]
            },
            "burnup": {
              "_output": [
                {
                  "_pltype": "array",
                  "_type": "double",
                  # "_do":
                  #  - copyarray MPACT/@temptable_polynomial,start=>0,stride=>3
                  "_value": copy_value,
                }
              ]
            },
            "a_linear": {
              "_output": [
                {
                  "_pltype": "array",
                  "_type": "double",
                  # "_do":
                  #  - copyarray MPACT/@temptable_polynomial,start=>1,stride=>3
                  "_value": copy_value,
                }
              ]
            },
            "b_quadratic": {
              "_output": [
                {
                  "_pltype": "array",
                  "_type": "double",
                  # "_do":
                  #  - copyarray MPACT/@temptable_polynomial,start=>2,stride=>3
                  "_value": copy_value,
                }
              ]
            },
            "boundary": {
              "_output": [
                {
                  "_pltype": "parameter",
                  "_type": "string",
                  # "_do":
                  #  - copy MPACT/$temptable_boundary
                  "_value": copy_value,
                }
              ]
            },
    "cmfd": {
      "_output": [
        {
          "_pltype": "list",
          "_value": copy_value,
        }
      ]
    },
        "cmfd": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy MPACT/$cmfd
              "_value": copy_value,
            }
          ]
        },
        "prolongation": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy MPACT/$prolongation
              "_value": copy_value,
            }
          ]
        },
        "solver": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy MPACT/$cmfd_solver
              "_value": copy_value,
            }
          ]
        },
        "linear_solver": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy MPACT/$cmfd_linear_solver
              "_value": copy_value,
            }
          ]
        },
        "petsc_linear_solver_method": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy MPACT/$petsc_linear_solver_method
              "_value": copy_value,
            }
          ]
        },
        "preconditioner": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy MPACT/$preconditioner
              "_value": copy_value,
            }
          ]
        },
        "eigen_solver": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy MPACT/$cmfd_eigen_solver
              "_value": copy_value,
            }
          ]
        },
        "k_shift": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "double",
              # "_do":
              #  - copy MPACT/$k_shift
              "_value": copy_value,
            }
          ]
        },
        "k_shift_1G": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "double",
              # "_do":
              #  - copy MPACT/$k_shift_1G
              "_value": copy_value,
            }
          ]
        },
        "cmfd_shift_method": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy MPACT/$cmfd_shift_method
              "_value": copy_value,
            }
          ]
        },
        "cmfd_shift_method_1G": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy MPACT/$cmfd_shift_method_1G
              "_value": copy_value,
            }
          ]
        },
        "cmfd_shift_c0": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "double",
              # "_do":
              #  - copy MPACT/$cmfd_shift_c0
              "_value": copy_value,
            }
          ]
        },
        "cmfd_relaxation": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "double",
              # "_do":
              #  - copy MPACT/$cmfd_relaxation
              "_value": copy_value,
            }
          ]
        },
        "ktol_1G": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy MPACT/$ktol_1G
              "_value": copy_value,
            }
          ]
        },
        "flxtol_1G": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy MPACT/$flxtol_1G
              "_value": copy_value,
            }
          ]
        },
        "max_1G_eig_its": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy MPACT/$max_1G_eig_its
              "_value": copy_value,
            }
          ]
        },
        "num_outers": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy MPACT/$cmfd_num_outers
              "_value": copy_value,
            }
          ]
        },
        "num_inners": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy MPACT/$cmfd_num_inners
              "_value": copy_value,
            }
          ]
        },
        "num_inners_1G": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy MPACT/$cmfd_num_inners_1G
              "_value": copy_value,
            }
          ]
        },
        "up_scatter": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy MPACT/$cmfd_up_scatter
              "_value": copy_value,
            }
          ]
        },
        "angle_decomp": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy MPACT/$cmfd_angle_decomp
              "_value": copy_value,
            }
          ]
        },
        "cmfd_ur": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "double",
              # "_do":
              #  - copy MPACT/$cmfd_ur
              "_value": copy_value,
            }
          ]
        },
        "subplane_target": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "double",
              # "_do":
              #  - copy MPACT/$subplane_target
              "_value": copy_value,
            }
          ]
        },
        "subplane_max": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "double",
              # "_do":
              #  - copy MPACT/$subplane_max
              "_value": copy_value,
            }
          ]
        },
        "num_subplanes": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy MPACT/$num_subplanes
              "_value": copy_value,
            }
          ]
        },
    "2d1d": {
      "_output": [
        {
          "_pltype": "list",
          "_value": copy_value,
        }
      ]
    },
        "splitTL": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "bool",
              # "_do":
              #  - copy MPACT/$split_TL
              "_value": copy_value,
            }
          ]
        },
        "TLtreatment": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy MPACT/$TL_treatment
              "_value": copy_value,
            }
          ]
        },
        "nodal_method": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy MPACT/$nodal_method
              "_value": copy_value,
            }
          ]
        },
        "under_relax": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "double",
              # "_do":
              #  - copy MPACT/$under_relax
              "_value": copy_value,
            }
          ]
        },
    "xs_library": {
      "_output": [
        {
          "_pltype": "list",
          "_value": copy_value,
        }
      ]
    },
        "xs_type": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy MPACT/$xs_type
              "_value": copy_value,
            }
          ]
        },
        "xs_filename": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy MPACT/$xs_filename
              "_value": copy_value,
            }
          ]
        },
        "ce_filename": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy MPACT/$ce_filename
              "_value": copy_value,
            }
          ]
        },
        "shield_method": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy MPACT/$shield_method
              "_value": copy_value,
            }
          ]
        },
        "shield_nbatch": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy MPACT/$shield_nbatch
              "_value": copy_value,
            }
          ]
        },
        "xsshielder": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy MPACT/$xs_shielder
              "_value": copy_value,
            }
          ]
        },
        "quasi_1D": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy MPACT/$quasi_1D
              "_value": copy_value,
            }
          ]
        },
        "res_up_scatter": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy MPACT/$res_up_scatter
              "_value": copy_value,
            }
          ]
        },
        "mats_file": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy MPACT/$mats_file
              "_value": copy_value,
            }
          ]
        },
        "subgroup_set": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "int",
              # "_do":
              #  - copy MPACT/$subgroup_set
              "_value": copy_value,
            }
          ]
        },
        "cat_onegroup": {
          "_output": [
            {
              "_pltype": "array",
              "_type": "int",
              # "_do":
              #  - copy MPACT/$cat_onegroup
              "_value": copy_value,
            }
          ]
        },
        "shld_range": {
          "_output": [
            {
              "_pltype": "array",
              "_type": "int",
              # "_do":
              #  - copy MPACT/$shld_range
              "_value": copy_value,
            }
          ]
        },
        "mod_mat": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy MPACT/$mod_mat
              "_value": copy_value,
            }
          ]
        },
    "transient": {
      "_output": [
        {
          "_pltype": "list",
          "_value": copy_value,
        }
      ]
    },
        "perturb_time_start": {
          "_output": [
            {
              "_pltype": "array",
              "_type": "double",
              # "_do":
              #  - copyarray MPACT/@perturb,start=>0,stride=>7
              "_value": copy_value,
            }
          ]
        },        "perturb_time_stop": {
          "_output": [
            {
              "_pltype": "array",
              "_type": "double",
              # "_do":
              #  - copyarray MPACT/@perturb,start=>1,stride=>7
              "_value": copy_value,
            }
          ]
        },        "perturb_time_step": {
          "_output": [
            {
              "_pltype": "array",
              "_type": "double",
              # "_do":
              #  - copyarray MPACT/@perturb,start=>2,stride=>7
              "_value": copy_value,
            }
          ]
        },
        "perturb_type": {
          "_output": [
            {
              "_pltype": "array",
              "_type": "string",
              # "_do":
              #  - copyarray MPACT/@perturb,start=>3,stride=>7
              "_value": copy_value,
            }
          ]
        },        "perturb_mat_init": {
          "_output": [
            {
              "_pltype": "array",
              "_type": "string",
              # "_do":
              #  - copyarray MPACT/@perturb,start=>4,stride=>7
              "_value": copy_value,
            }
          ]
        },        "perturb_mat_start": {
          "_output": [
            {
              "_pltype": "array",
              "_type": "string",
              # "_do":
              #  - copyarray MPACT/@perturb,start=>5,stride=>7
              "_value": copy_value,
            }
          ]
        },        "perturb_mat_stop": {
          "_output": [
            {
              "_pltype": "array",
              "_type": "string",
              # "_do":
              #  - copyarray MPACT/@perturb,start=>6,stride=>7
              "_value": copy_value,
            }
          ]
        },
        "timestep_dt": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "double",
              # "_do":
              #  - copy MPACT/$"timestep":0
              "_value": copy_value,
            }
          ]
        },        "timestep_dt_min": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "double",
              # "_do":
              #  - copy MPACT/$"timestep":1
              "_value": copy_value,
            }
          ]
        },        "timestep_dt_max": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "double",
              # "_do":
              #  - copy MPACT/$"timestep":2
              "_value": copy_value,
            }
          ]
        },
        "tml": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "bool",
              # "_do":
              #  - copy MPACT/$tml
              "_value": copy_value,
            }
          ]
        },
        "prompt": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "bool",
              # "_do":
              #  - copy MPACT/$prompt
              "_value": copy_value,
            }
          ]
        },
        "accel": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "bool",
              # "_do":
              #  - copy MPACT/$accel
              "_value": copy_value,
            }
          ]
        },
        "delayenergy": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "bool",
              # "_do":
              #  - copy MPACT/$delayenergy
              "_value": copy_value,
            }
          ]
        },
        "transmethod": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "string",
              # "_do":
              #  - copy MPACT/$"transmethod":0
              "_value": copy_value,
            }
          ]
        },
        "theta_order": {
          "_output": [
            {
              "_pltype": "parameter",
              "_type": "double",
              # "_do":
              #  - copy MPACT/$"transmethod":1
              "_value": copy_value,
            }
          ]
        },
  }
}
