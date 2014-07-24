#!/usr/bin/python

import distutils.sysconfig
import site
import sys

print "\nsite.getsitepackages():" 
for dir in site.getsitepackages():
    print "  " + dir

print "\n  Compare with distutils.sysconfig.get_python_lib():"
print "    " + distutils.sysconfig.get_python_lib()

print "\n  Compare alse with sys.prefix"
print "    " + sys.prefix
