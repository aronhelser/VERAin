from __future__ import absolute_import, division, print_function

from Templates.Utils import *

COBRATF = {
  "_content": {
    "nfuel": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "int",
          # "_do":
          #  - copy COBRATF/$nfuel
          "_value": copy_value,
        }
      ]
    },
    "imox": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "int",
          # "_do":
          #  - copy COBRATF/$imox
          "_value": copy_value,
        }
      ]
    },
    "nc": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "int",
          # "_do":
          #  - copy COBRATF/$nc
          "_value": copy_value,
        }
      ]
    },
    "chf": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "int",
          # "_do":
          #  - copy COBRATF/$chf
          "_value": copy_value,
        }
      ]
    },
    "debug": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "int",
          # "_do":
          #  - copy COBRATF/$debug
          "_value": copy_value,
        }
      ]
    },
    "irfc": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "int",
          # "_do":
          #  - copy COBRATF/$irfc
          "_value": copy_value,
        }
      ]
    },
    "dhfrac": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy COBRATF/$dhfrac
          "_value": copy_value,
        }
      ]
    },
    "beta_htc": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy COBRATF/$beta_htc
          "_value": copy_value,
        }
      ]
    },
    "hgap": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy COBRATF/$hgap
          "_value": copy_value,
        }
      ]
    },
    "epso": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy COBRATF/$epso
          "_value": copy_value,
        }
      ]
    },
    "oitmax": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "int",
          # "_do":
          #  - copy COBRATF/$oitmax
          "_value": copy_value,
        }
      ]
    },
    "iitmax": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "int",
          # "_do":
          #  - copy COBRATF/$iitmax
          "_value": copy_value,
        }
      ]
    },
    "dtmin": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy COBRATF/$dtmin
          "_value": copy_value,
        }
      ]
    },
    "dtmax": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy COBRATF/$dtmax
          "_value": copy_value,
        }
      ]
    },
    "tend": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy COBRATF/$tend
          "_value": copy_value,
        }
      ]
    },
    "rtwfp": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy COBRATF/$rtwfp
          "_value": copy_value,
        }
      ]
    },
    "maxits": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "int",
          # "_do":
          #  - copy COBRATF/$maxits
          "_value": copy_value,
        }
      ]
    },
    "courant": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy COBRATF/$courant
          "_value": copy_value,
        }
      ]
    },
    "maps_filename": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy COBRATF/$maps_filename
          "_value": copy_value,
        }
      ]
    },
    "heated_elements_type": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "int",
          # "_do":
          #  - copy COBRATF/$heated_elements_type
          "_value": copy_value,
        }
      ]
    },
    "heater_tube_id": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy COBRATF/$heater_tube_id
          "_value": copy_value,
        }
      ]
    },
    "heater_tube_od": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy COBRATF/$heater_tube_od
          "_value": copy_value,
        }
      ]
    },
    "heater_tube_pitch": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy COBRATF/$heater_tube_pitch
          "_value": copy_value,
        }
      ]
    },
    "solver": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "int",
          # "_do":
          #  - copy COBRATF/$solver
          "_value": copy_value,
        }
      ]
    },
    "parallel": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "int",
          # "_do":
          #  - copy COBRATF/$parallel
          "_value": copy_value,
        }
      ]
    },
    "global_energy_balance": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy COBRATF/$global_energy_balance
          "_value": copy_value,
        }
      ]
    },
    "global_mass_balance": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy COBRATF/$global_mass_balance
          "_value": copy_value,
        }
      ]
    },
    "fluid_energy_storage": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy COBRATF/$fluid_energy_storage
          "_value": copy_value,
        }
      ]
    },
    "solid_energy_storage": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy COBRATF/$solid_energy_storage
          "_value": copy_value,
        }
      ]
    },
    "mass_storage": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy COBRATF/$mass_storage
          "_value": copy_value,
        }
      ]
    },
    "Tcool_criteria": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy COBRATF/$Tcool_criteria
          "_value": copy_value,
        }
      ]
    },
    "Tsolid_criteria": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy COBRATF/$Tsolid_criteria
          "_value": copy_value,
        }
      ]
    },
    "void_criteria": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy COBRATF/$void_criteria
          "_value": copy_value,
        }
      ]
    },
    "pressure_criteria": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy COBRATF/$pressure_criteria
          "_value": copy_value,
        }
      ]
    },
    "vliq_criteria": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy COBRATF/$vliq_criteria
          "_value": copy_value,
        }
      ]
    },
    "vvap_criteria": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy COBRATF/$vvap_criteria
          "_value": copy_value,
        }
      ]
    },
    "vdrop_criteria": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy COBRATF/$vdrop_criteria
          "_value": copy_value,
        }
      ]
    },
    "Tcoola_criteria": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy COBRATF/$Tcoola_criteria
          "_value": copy_value,
        }
      ]
    },
    "Tsolida_criteria": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy COBRATF/$Tsolida_criteria
          "_value": copy_value,
        }
      ]
    },
    "pressurea_criteria": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy COBRATF/$pressurea_criteria
          "_value": copy_value,
        }
      ]
    },
    "vliqa_criteria": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy COBRATF/$vliqa_criteria
          "_value": copy_value,
        }
      ]
    },
    "vvapa_criteria": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy COBRATF/$vvapa_criteria
          "_value": copy_value,
        }
      ]
    },
    "vdropa_criteria": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy COBRATF/$vdropa_criteria
          "_value": copy_value,
        }
      ]
    },
    "use_sol_stop_crit": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "int",
          # "_do":
          #  - copy COBRATF/$use_sol_stop_crit
          "_value": copy_value,
        }
      ]
    },
    "edit_gaps": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "int",
          # "_do":
          #  - copy COBRATF/$edit_gaps
          "_value": copy_value,
        }
      ]
    },
    "edit_channels": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "int",
          # "_do":
          #  - copy COBRATF/$edit_channels
          "_value": copy_value,
        }
      ]
    },
    "edit_rods": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "int",
          # "_do":
          #  - copy COBRATF/$edit_rods
          "_value": copy_value,
        }
      ]
    },
    "edit_dnb": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "int",
          # "_do":
          #  - copy COBRATF/$edit_dnb
          "_value": copy_value,
        }
      ]
    },
    "edit_convergence": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "int",
          # "_do":
          #  - copy COBRATF/$edit_convergence
          "_value": copy_value,
        }
      ]
    },
    "edit_hdf5": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "int",
          # "_do":
          #  - copy COBRATF/$edit_hdf5
          "_value": copy_value,
        }
      ]
    },
    "edit_fluid_vtk": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "int",
          # "_do":
          #  - copy COBRATF/$edit_fluid_vtk
          "_value": copy_value,
        }
      ]
    },
    "edit_rod_vtk": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "int",
          # "_do":
          #  - copy COBRATF/$edit_rod_vtk
          "_value": copy_value,
        }
      ]
    },
    "proc_per_assem": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "int",
          # "_do":
          #  - copy COBRATF/$proc_per_assem
          "_value": copy_value,
        }
      ]
    },
    "gap_model": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy COBRATF/$gap_model
          "_value": copy_value,
        }
      ]
    },
    "boil_ht_cor": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy COBRATF/$boil_ht_cor
          "_value": copy_value,
        }
      ]
    },
    "property_evaluations": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy COBRATF/$property_evaluations
          "_value": copy_value,
        }
      ]
    },
    "k_void_drift": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy COBRATF/$k_void_drift
          "_value": copy_value,
        }
      ]
    },
    "beta_sp": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy COBRATF/$beta_sp
          "_value": copy_value,
        }
      ]
    },
    "crud": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #  - copy COBRATF/$crud
          "_value": copy_value,
        }
      ]
    },
  }
}
