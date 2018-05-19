#!/usr/bin/python

import sys

#
#   The type of sys.modules is a dictionary:
#
print(type(sys.modules)) # <class 'dict'>

#
#   Print names of imported modules.
#
for module_name in sys.modules:
    print(module_name)

#
# sys.modules maps from strings to 'class modules':
#
print(type(sys.modules['sys'])) # <class 'module'>
