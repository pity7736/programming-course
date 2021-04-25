# Data type

## Definitions

**Variable**: it's a memory space that stores a data. Value can change at runtime.

**Data type**: it's data attribute that determines the domain of a variable and what messages can be sent to it.

**Domain**: it's the possible values of a specific data type.

## Types

* Integers (int)
* Floats (float)
* Complex (complex)
* Sequences
* Strings (str)
* Tuples (tuple)
* Lists (list)
* Dictionaries (dict)

### Integers

Integers are a number representation without fractional part (e.g. `1`, `5`, `10`).
It's handled with `int` object.

### Floats

Floats are a number representation with fractional part (e.g. `1.0`, `5.0`, `10.0`, `11.5`).
It's handled with `float` object.

### Complex

Complex are a number representation with a real and imaginary part which are each a float number.
e.g `3 + 6j`. It's handled with `complex`object. 

### Sequences

Sequences are not a specific type itself but it's an abstract type for strings, lists, tuples and so on.

See [common sequence operations](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations).

### Strings

String are a text representation handled with `str` object. Strings are immutable sequence of characters (unicode code).
String are written in several ways:

* Single quotes: 'hi world'.
* Double quotes: "hi world".
* Triple quotes: '''hi world''' or """hi world"""".

See [string methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

### Tuples

Tuples are heterogeneous and immutable sequences. Tuples may be constructed in several ways:

* Using a pair of parentheses to denote the empty tuple: `()`
* Using a trailing comma for a singleton tuple: `a,` or `(a,)`
* Separating items with commas: `a, b, c` or `(a, b, c)`
* Using the tuple() built-in: `tuple()` or `tuple(iterable)`

### Lists

Lists are heterogeneous and mutable sequences. Lists may be constructed in several ways:

* Using a pair of square brackets to denote the empty list: `[]`
* Using square brackets, separating items with commas: `[a]`, `[a, b, c]`
* Using a list comprehension: `[x for x in iterable]`
* Using the type constructor: `list()` or `list(iterable)`

See [list methods](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

### Dictionaries

Dictionaries are mutable arrays of key-value pairs. Dictionaries may be constructed in several ways:

* Use a comma-separated list of key: value pairs within braces: `{'jack': 4098, 'sjoerd': 4127}` or `{4098: 'jack', 4127: 'sjoerd'}`
* Use a dict comprehension: `{}`, `{x: x ** 2 for x in range(10)}`
* Use the type constructor: `dict()`, `dict([('foo', 100), ('bar', 200)])`, `dict(foo=100, bar=200)`

[More information about dictionaries](https://docs.python.org/3/library/stdtypes.html#dict)
