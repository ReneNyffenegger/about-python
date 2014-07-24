#!/usr/bin/python

import site
import distutils.sysconfig

print "\nsite.getsitepackages():" 
for dir in site.getsitepackages():
    print "  " + dir

print "\nCompare with distutils.sysconfig.get_python_lib():"
print "  " + distutils.sysconfig.get_python_lib()
