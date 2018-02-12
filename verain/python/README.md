# VERAin Python

A python script to convert VERA `inp` to VERA `xml` format.

## Requirements

Python version 2.7 or 3.5+ are required. The only non-standard python package used by the script is `pyparsing`. It can be installed using `pip`:

```
pip install -u pip
pip install pyparsing
```

## Command line

The parser is run from the command line, like this:

```
  python $PYPATH/inp2xml.py --in=p9.inp --out=p9.xml
```

where `$PYPATH` is the path to the script.

## Design goals

The converter is written in Python, a more friendly and familiar language than Perl for most researchers who might be working with simulation codes.

The converter uses PyParsing, which has a structure which is more readable and understandable than regular expressions, so hopefully will be more easily modified and maintained.

Templates handle each section of the input file. They map directly from input keywords to output, so a new input card can be specified with its verification and output in one place.

## Pyparsing

Pyparsing is a native Python parser that allows easy translation from a parsing grammer to python code. From the [wiki](http://pyparsing.wikispaces.com/):

> The Python representation of the grammar is quite readable, owing to the self-explanatory class names, and the use of '+', '|' and '^' operators.

[This tutorial](http://infohost.nmt.edu/tcc/help/pubs/pyparsing/web/index.html#intro) provides good examples and reference information.

The main grammar is contained in `inp2xml.py:VeraInConverter:inpfile_BNF()`.

## Templates

Each section of the .inp file has its own tempate. A template file is written in Python, and defines a dictionary which maps card names to output. The simplest section is CASEID, and this section of the input file looks like this:

```
[CASEID]
  title 'CASL AMA Problem 9 - Watts Bar Unit 1 Cycle 1 Depletion - Public'
```

The one card in this section is `title`, with a description for its value.

This section produces this output:

```xml
<ParameterList name="CASEID">
  <Parameter name="case_id" type="string" value="CASL AMA Problem 9 - Watts Bar Unit 1 Cycle 1 Depletion - Public"/>
</ParameterList>
```

Finally here's the template that specifies this conversion:

```python
from Templates.Utils import *

CASEID = {
  "_pltype": "list",
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
```

The output of the converter is an XML file in *ParameterList* format, defined in the [Trilinos Teuchos package](https://trilinos.org/docs/dev/packages/teuchos/doc/html/index.html#TeuchosParameterList_src).

The CASEID section will produce a list, with the content defined by the dictionary `_content`. Each card name is unique, so it is a key in the dictionary. CASEID has only one keyword, `title`. When it is encountered, it will produce a list of parameters defined in the `output` list. Here, you can see this is only one `Parameter` output, named `case_id`, with type `string` and with the value copied from the input file.

If the `_name` is omitted, the input keyword is used as its name (in this case it would be `title`).

`_type` can be `int`, `bool`, `double` or `string`.

`_pltype` can be `parameter` or `array`. An array includes braces `{ }` around a list of one or more values, separated by commas.

The `_value` entry specifies how to extract the actual data value from the input. `copy_value` is actually a function, defined in the `Templates/Utils.py` file/module. This copies the next token (number or word) after the card name. There are several other functions defined there, to handle more comples values, like arrays. The converter supplies a list of tokens that belong to the current card to these functions. For instance: 

* `"_value": [copy_value, 1]` will copy the second token (with index 1) from the card. The use of a Python list allows us to pass parameters to the function.
* `"_value": [copy_array, slice(1, None, 2)]` copies a whole list. The `slice()` argument says to be selective - start from index 1, go to the end (`None`), and skip every other element (step of 2). That means `slice(1, None, 2)` will copy tokens 1,3,5... from this card.
* `"_value": [assembly_map, "ref:npin:0"]` More complex cards can be handled with specialized functions, like the core or assembly maps. This also illustrates a reference parameter, discussed next.

### Nested lists

The most common form of nest lists is just to group some cards into a list for output. Use `_inlist` to accomplish this:
```python
    "automesh_bounds": {
      "_inlist": "mesh",
      "_output": [
        {
          "_name": "automesh_bounds_min",
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy MPACT/$"automesh_bounds":0
          "_value": [copy_value, 0],
        },
        {
          "_name": "automesh_bounds_max",
          "_pltype": "parameter",
          "_type": "double",
          # "_do":
          #  - copy MPACT/$"automesh_bounds":1
          "_value": [copy_value, 1],
        }
      ]
    },
```

In this case, the parameters `automesh_bounds_min` and `automesh_bounds_max` will be output inside the ParameterList `automesh_bounds`. Nested lists can be accomplished by listing two names, `"_inlist": "parallel_env,graph"`. A few cards have their output duplicated, both in a sublist and not. These use `"_notInList": True`.

More complex is the card that results in a list-of-lists. A straightforward example is materials, specified as `mat` cards in the core or assemblies. The template, from `CellMaps.py`, is:

```python
    "mat": {
      "_pltype": "list",
      "_name": "Materials",
      "_listName": "Material_%s",
      "_output": [
        {
          "_name": "density",
          "_pltype": "parameter",
          "_type": "double",
          "_value": [copy_value, 1],
        },
        {
          "_name": "key_name",
          "_pltype": "parameter",
          "_type": "string",
          "_value": [copy_value, 0],
        },
        {
          "_name": "mat_fracs",
          "_pltype": "array",
          "_type": "double",
          "_optional": True,
          # almost works, but sometimes we need a default frac
          # "_value": [copy_array_before_val, '/', slice(3, None, 2)],
          "_value": mat_fracs,
        },
        {
          "_name": "mat_names",
          "_pltype": "array",
          "_type": "string",
          "_optional": True,
          "_value": [copy_array_before_val, '/', slice(2, None, 2)],
        },
        {
          "_name": "thexp",
          "_pltype": "parameter",
          "_type": "double",
          "_optional": True,
          "_value": [extract_param, "thexp"],
        },
      ]
    },
```

Everything is grouped into the `Materials` list. Then each `mat` card gets its own sub-list. Each `mat` card has a tag, like `air` or `aic`, which is used both in the sub-list name and as the `key_name` parameter. The other card values are extracted as expected, some using more advanced `_value` functions.

This input:

```
   mat air      1.189E-03  n-14   0.7649  ! engineeringtoolbox.com
                           o-16   0.2351  ! normalized to 1.0 @ 20C density (smeared)
 
   mat aic         10.2    ag-107 4.11010E-01  ! SCALE 6.2
                           ag-109 3.88990E-01 
                           in-113 6.32772E-03 
                           in-115 1.43672E-01 
                           cd-00  5.00000E-02  ! combined cadmium for MPACT
                           / thexp=6.9
```

Results in output like this:

```xml
<ParameterList name="Materials">
  <ParameterList name="Material_air">
    <Parameter name="density" type="double" value="0.001189"/>
    <Parameter name="key_name" type="string" value="air"/>
    <Parameter name="mat_fracs" type="Array(double)" value="{0.7649,0.2351}"/>
    <Parameter name="mat_names" type="Array(string)" value="{n-14,o-16}"/>
  </ParameterList>
  <ParameterList name="Material_aic">
    <Parameter name="density" type="double" value="10.2"/>
    <Parameter name="key_name" type="string" value="aic"/>
    <Parameter name="mat_fracs" type="Array(double)" value="{0.41101,0.38899,0.00632772,0.143672,0.05}"/>
    <Parameter name="mat_names" type="Array(string)" value="{ag-107,ag-109,in-113,in-115,cd-00}"/>
    <Parameter name="thexp" type="double" value="6.9"/>
  </ParameterList>
</ParameterList>
```

### Conditional output

The `mat` processing in the previous section also illustrates how optional output works. If the template output includes `"_optional": True`, like the `thexp` output above, and the `_value` method returns `None`, the parameter will not be output.

As an example, the `mat` card for `water`:

```
   mat water       0.743   h-1    1.11915E-01  ! SCALE 6.2 
                           o-16   8.88085E-01  ! density at 565K
```

doesn't output expansion:

```xml
  <ParameterList name="Material_water">
    <Parameter name="density" type="double" value="0.743"/>
    <Parameter name="key_name" type="string" value="water"/>
    <Parameter name="mat_fracs" type="Array(double)" value="{0.111915,0.888085}"/>
    <Parameter name="mat_names" type="Array(string)" value="{h-1,o-16}"/>
  </ParameterList>
```

Cards can also be output depending on the values of other cards. In `CellMaps.py`, cells are only output if they are used in rodmaps, which in turn are only output if they are used in the `axial` card for the current list item. This is accomplished through use of reference parameters (explained next) and a `_condition` entry, which calls a method which should return true if the card should be output in the current context.

Finally, the `CellMaps` template includes this directive: `"_sectionParams": ["axial"]`. This tells the converter that one assembly (or detector, control, insert) should be output per `axial` card encountered. The current `axial` card then determines which rodmaps, fuels and cells are output.

### Reference params

A `_refParam` allows the value method of a card to get information from another card. For instance, the `assembly_map` needs to know how may pins to expect, so it lists a `ref` as one of its arguments: `"_value": [assembly_map, "ref:npin:0"]`

The converter extracts the values to substitute for this reference parameter in two ways. First, the `CellMaps` section includes this:

```python
CellMaps = {
  "_refParams": ["npin"],
}
```

The converter will extract the value of the `npin` card and save it to substitute for a reference parameter.

Secondly, if only a piece of a card is desired, like when we need to know just the tags used in the axial card, it's specified as part of the `_output`, and it uses a different function from `Utils`:

```python
    "axial": {
      "_matchSection": True,
      "_output": [
        {
          "_name": "axial_labels",
          "_pltype": "array",
          "_type": "string",
          "_refParam": [extract_array, slice(2, None, 2)],
          "_value": [copy_array, slice(2, None, 2)],
        },
      ]
    }
```

It is important that the reference parameter be defined before the section that tries to use it. To ensure this, the `_order` directive is included for some templates. For instance, the `CellMap` template includes `"_order": ["axial", "rodmap", "fuel", "cell"]`. Then `axial` will be processed before `rodmap`, defining the reference parameter `axial_labels`, so that only the `rodmap`s used in the current `axial` card will be output.

### Composition

Assemblies, controls, detectors and inserts all share the same cards for materials, cells, rodmaps, and axial definitions. This commonality is defined in CellMaps.py, then incorporated into the different sections like this:

```python
from Templates.CellMaps import CellMaps

_assemblyDiff = {
  "_groupName": "ASSEMBLIES",
  "_sectionName": "Assembly_%s",
  "_order": ["axial", "lattice", "rodmap", "fuel", "cell"],
}

ASSEMBLY = copy.deepcopy(CellMaps)
ASSEMBLY.update(_assemblyDiff)

_assemblyContentDiff = {
  ...
}

ASSEMBLY["_content"].update(_assemblyContentDiff)
```

The differences for the `ASSEMBLY` section are copied over or added to those defined in the CellMaps module.

### Includes

The `include` card specifies a filename to be included in the current file. The converter does this as a pre-pass, substituting the text of the include file into the input file before it is parsed. 

The converter looks for the include file in three places:
* next to the input file
* next to the converter script file
* in the perl script init directory, `../scripts/Init`, relative to the converter script file.

### Defaults

Defaults work similarly to an include card - the converter looks for an `.ini` file named after the section, like `CORE.ini`, in the same place it looks for include files. If it finds one, it substitutes the text immediately after the section header. The perl script directory includes defaults for `CORE`, `INSILICO`, `MPACT`, and `SHIFT`.
