from __future__ import absolute_import, division, print_function

from Templates.Utils import *

STATE = {
  "_pltype": "list",
  # "_do":
  #   - setdb MAIN_DB
  #    - setvar _path,%STATE/*/$/@rodbank,apply=>&pathfind
  #    - getvar _path,apply=>'my @value=split(/\//,shift @_); splice(@value,2,1)';
  #    - getvar _path,apply=>&pathlevel,arg=>3

  # "_tr":
  #   "_name": "_loop"
  #   "_content": ""%STATE

    # State_(_loop)"":
      # "_pltype": "list"
      # "_do":
      #   - setdb MAIN_DB

  "_content": {

    "id": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #   - copy %STATE/$(_loop)/$id
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
          #   - copy %STATE/$(_loop)/$title
          "_value": copy_value,
        }
      ]
    },
    "power": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #   - copy %STATE/$(_loop)/$power
          "_value": copy_value,
        }
      ]
    },
    "flow": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #   - copy %STATE/$(_loop)/$flow
          "_value": copy_value,
        }
      ]
    },
    "bypass": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #   - copy %STATE/$(_loop)/$bypass
          "_value": copy_value,
        }
      ]
    },
    "xenon": {
      "_output": [
        {
          "_name": "xenopt",
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #   - copy %STATE/$(_loop)/$xenon
          "_value": copy_value,
        }
      ]
    },
    "samopt": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #   - copy %STATE/$(_loop)/$samar
          "_value": copy_value,
        }
      ]
    },
    "rlx_xesm": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #   - copy %STATE/$(_loop)/$rlx_xesm
          "_value": copy_value,
        }
      ]
    },
    "rodbank": {
      "_output": [
        {
          "_name": "bank_labels",
          "_pltype": "array",
          "_type": "string",
          # "_do":
          #   - copyarray %STATE/$(_loop)/@rodbank,select=>even
          "_value": [copy_array, slice(0, None, 2)],
        },
        {
          "_name": "bank_pos",
          "_pltype": "array",
          "_type": "int",
          # "_do":
          #   - copyarray %STATE/$(_loop)/@rodbank,select=>odd
          "_value": [copy_array, slice(1, None, 2)],
        }
      ]
    },
    "boron": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #   - copy %STATE/$(_loop)/$boron
          "_value": copy_value,
        }
      ]
    },
    "b10": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #   - copy %STATE/$(_loop)/$"b10":0
          "_value": [copy_value, 0],
        },
        {
          "_name": "b10_depl",
          "_pltype": "parameter",
          "_type": "bool",
          # "_do":
          #   - copy %STATE/$(_loop)/$"b10":1
          "_value": [copy_value, 1],
        }
      ]
    },
    "tinlet": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #   - tocelsius %STATE/$(_loop)/@tinlet
          "_value": toCelsius,
        }
      ]
    },
    "pressure": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #   - copy %STATE/$(_loop)/$pressure,apply=>($_[0])*0.00689475729
          "_value": [copy_value_mult, 0, 0.00689475729],
        }
      ]
    },
    "search": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #   - copy %STATE/$(_loop)/$search
          "_value": copy_value,
        }
      ]
    },
    "search_bank": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #   - copy %STATE/$(_loop)/$search_bank
          "_value": copy_value,
        }
      ]
    },
    "kcrit": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #   - copy %STATE/$(_loop)/$kcrit
          "_value": copy_value,
        }
      ]
    },
    "deplete": {
      "_output": [
        {
          "_pltype": "array",
          "_type": "double",
          # "_do":
          #   - copyarray %STATE/$(_loop)/@deplete,start=>1
          "_value": [copy_array, slice(1, None)],
        },
        {
          "_name": "deplete_units",
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #   - copy %STATE/$(_loop)/@"deplete":0
          "_value": [copy_value, 0],
        }
      ]
    },
    "edit": {
      "_output": [
        {
          "_pltype": "array",
          "_type": "string",
          # "_do":
          #   - copyarray %STATE/$(_loop)/$edit
          "_value": copy_value,
        }
      ]
    },
    "tfuel": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #   - tocelsius %STATE/$(_loop)/@tfuel,apply=>($_[0]+273.15)
          "_value": toKelvin,
        }
      ]
    },
    "modden": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #   - copy %STATE/$(_loop)/$modden
          "_value": copy_value,
        }
      ]
    },
    "feedback": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #   - copy %STATE/$(_loop)/$feedback
          "_value": copy_value,
        }
      ]
    },
    "thexp": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #   - copy %STATE/$(_loop)/$thexp
          "_value": copy_value,
        }
      ]
    },
    "thexp_tfuel": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #   - tocelsius %STATE/$(_loop)/@thexp_tfuel,apply=>($_[0]+273.15)
          "_value": toKelvin,
        }
      ]
    },
    "thexp_tclad": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #   - tocelsius %STATE/$(_loop)/@thexp_tclad,apply=>($_[0]+273.15)
          "_value": toKelvin,
        }
      ]
    },
    "thexp_tmod": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #   - tocelsius %STATE/$(_loop)/@thexp_tmod,apply=>($_[0]+273.15)
          "_value": toKelvin,
        }
      ]
    },
    "sym": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #   - copy %STATE/$(_loop)/$sym
          "_value": copy_value,
        }
      ]
    },
    "reset_sol": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "bool",
          # "_do":
          #   - copy %STATE/$(_loop)/$reset_sol
          "_value": copy_value,
        }
      ]
    },
    "op_date": {
      "_output": [
        {
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #   - copy %STATE/$(_loop)/$op_date
          "_value": copy_value,
        }
      ]
    },
    "restart_shuffle": {
      "_output": [
        {
          "_name": "restart_shuffle_file",
          "_pltype": "array",
          "_type": "string",
          # "_do":
          #   - copyarray %STATE/$(_loop)/@restart_shuffle,select=>even
          "_value": [copy_array, slice(0, None, 2)],
        },
        {
          "_name": "restart_shuffle_label",
          "_pltype": "array",
          "_type": "string",
          # "_do":
          #   - copyarray %STATE/$(_loop)/@restart_shuffle,select=>odd
          "_value": [copy_array, slice(1, None, 2)],
        }
      ]
    },
    "restart_write": {
      "_output": [
        {
          "_name": "restart_write_file",
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #   - copy %STATE/$(_loop)/@"restart_write":0
          "_value": [copy_value, 0],
        },
        {
          "_name": "restart_write_label",
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #   - copy %STATE/$(_loop)/@"restart_write":1
          "_value": [copy_value, 1],
        }
      ]
    },
    "restart_read": {
      "_output": [
        {
          "_name": "restart_read_file",
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #   - copy %STATE/$(_loop)/@"restart_read":0
          "_value": [copy_value, 0],
        },
        {
          "_name": "restart_read_label",
          "_pltype": "parameter",
          "_type": "string",
          # "_do":
          #   - copy %STATE/$(_loop)/@"restart_read":1
          "_value": [copy_value, 1],
        }
      ]
    },
    "shuffle_label": {
      "_output": [
        {
          "_pltype": "array",
          "_type": "string",
          # "_do":
          #   - coremapmap CORE/$size,CORE/@core_shape,%STATE/$(_loop)/@shuffle_label,CORE/$bc_sym,expand=>0,ignore=>'-'
          "_value": copy_value,
        }
      ]
    },
    "tinlet_dist": {
      "_output": [
        {
          "_pltype": "array",
          "_type": "double",
          # "_do":
          #   - coremapmap CORE/$size,CORE/@core_shape,%STATE/$(_loop)/@tinlet_dist,CORE/$bc_sym
          "_value": copy_value,
        }
      ]
    },
    "void_map": {
      "_output": [
        {
          "_pltype": "array",
          "_type": "double",
          # "_do":
          #   - coremapmap CORE/$size,CORE/@core_shape,%STATE/$(_loop)/@void,CORE/$bc_sym
          "_value": copy_value,
        }
      ]
    },
    "flow_dist": {
      "_output": [
        {
          "_pltype": "array",
          "_type": "double",
          # "_do":
          #   - coremapmap CORE/$size,CORE/@core_shape,%STATE/$(_loop)/@flow_dist,CORE/$bc_sym
          "_value": copy_value,
        }
      ]
    },
    "cool_chem": {
      "_output": [
        {
          "_name": "h_conc",
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #   - copy %STATE/$(_loop)/$"cool_chem":0
          "_value": [copy_value, 0],
        },
        {
          "_name": "li_conc",
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #   - copy %STATE/$(_loop)/$"cool_chem":1
          "_value": [copy_value, 1],
        },
        {
          "_name": "ni_sol",
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #   - copy %STATE/$(_loop)/$"cool_chem":2
          "_value": [copy_value, 2],
        },
        {
          "_name": "ni_par",
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #   - copy %STATE/$(_loop)/$"cool_chem":3
          "_value": [copy_value, 3],
        },
        {
          "_name": "fe_sol",
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #   - copy %STATE/$(_loop)/$"cool_chem":4
          "_value": [copy_value, 4],
        }
      ]
    },
  }
}
