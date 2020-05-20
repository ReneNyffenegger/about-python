#
#      To be called either so
#
#         python stdout_or_file.py
#
#      or so
#
#         python stdout_or_file.py some-file-name
#
#      -------------------------------------------
#
#      If no file name is specified, the script will
#      print three lines to stdout, otherwise, it
#      will print these lines into the file given
#      as first argument to the script.
#
#
import sys

if len(sys.argv) > 1:
   print "Writing to file " + sys.argv[1]

   f_ = open(sys.argv[1], 'w')

else:

   f_ = sys.stdout

f_.write('Line one\n')
f_.write('Line two\n')
f_.write('Line three')
