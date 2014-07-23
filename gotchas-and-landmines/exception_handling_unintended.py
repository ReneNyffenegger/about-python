#
#   http://stackoverflow.com/a/4403680/180275
#
#   Compare with exception_handling_intended.py

try:
    int("z")
except IndexError, ValueError:
    print "exception";          # not caught!
