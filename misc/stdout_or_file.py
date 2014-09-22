import sys

if len(sys.argv) > 1:
   print "Writing to file " + sys.argv[1]

   f_ = open(sys.argv[1], 'w')

else:

   f_ = sys.stdout

f_.write('Line one\n')
f_.write('Line two\n')
f_.write('Line three')
