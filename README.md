# variable_type_hint_writer

Automatically write type hints and return types for all the python functions of a given file.

# How does it work?

There are two main components to this. 
1. Large Language Model
2. Abstract Tree Syntax

Most parameter types are handled by pickled dictionaries that i made from every possible assignment variable in all of python history. If the name of the variable matches any
variable given every with that type, it will asign the type to it.

For return types, it takes the function node and follows the return types to there variable or literal returns.

