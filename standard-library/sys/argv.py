import sys

print
print "Script was called with %d argument(s)" % (len(sys.argv) - 1)
print "The script name is: ", sys.argv[0]


if len(sys.argv) - 1:

   print
   print "The argument(s) are:"

   for arg in sys.argv[1:]:
       print "  ", arg

print
