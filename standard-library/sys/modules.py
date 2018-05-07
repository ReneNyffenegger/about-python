#!/usr/bin/python

import sys

#
# The type of sys.modules is a dictionary:
#
print(type(sys.modules)) # <class 'dict'>

#
# sys.modules maps from strings to 'class modules':
#
for mod in sys.modules:
    print(type(sys.modules[mod]))
