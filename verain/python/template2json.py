# Export the simulator templates to a pure JSON object, so they
# can be used by the 'vera' type in Simput to create a UI
# automatically for these parameters.
# See https://github.com/kitware/simput, types/vera/src/simModel.js
from __future__ import absolute_import, division, print_function

import os, json

from Templates.SHIFT import SHIFT
from Templates.MPACT import MPACT
from Templates.COBRATF import COBRATF
from Templates.INSILICO import INSILICO

templateNames = {
    # Simulator code config blocks
    "SHIFT": SHIFT,
    "COBRATF": COBRATF,
    "INSILICO": INSILICO,
    "MPACT": MPACT,
}

class FuncEncoder(json.JSONEncoder):
    def default(self, obj):
        if callable(obj):
            # replace functions by their name
            return obj.__name__
        elif type(obj) is slice:
            # slice is a built-in, replace by string.
            return str(obj)
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)

def parse( template, name ):
    print( name )
    return json.dumps(template, cls=FuncEncoder, indent=2)


if __name__ == "__main__":
    for key in templateNames:
        result = parse(templateNames[key], key)
        if result:
            outFile = open(key + ".json", "w")
            outFile.write(result)
            outFile.close()


