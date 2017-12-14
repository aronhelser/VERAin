from __future__ import absolute_import, division, print_function

from Templates.Utils import *

CASEID = {
  "_pltype": "list",
  # _do:
  #   - setdb MAIN_DB
  "_content": {
    "title": {
      "_output": [
        {
          "_name": "case_id",
          "_pltype": "parameter",
          "_type": "string",
          "_value": copy_value,
        }
      ]
    }
  }
}
