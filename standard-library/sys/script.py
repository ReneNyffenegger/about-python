#!/usr/bin/python

import sys

print "\npaths in sys.path:"
for dir in sys.path:
    print "  " + dir


print "\nPrint without newlines:"
sys.stdout.write('  ')
for i in range(10):
    sys.stdout.write (str(i) + " ")

print "\n\nsys.prefix = " + sys.prefix
print "  Compare with distutils.sysocnifg.get_python_lib() and site.getsitepackages()"

print "\ngetdefaultencoding: " + sys.getdefaultencoding()
