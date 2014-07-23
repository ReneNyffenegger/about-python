#
#   http://stackoverflow.com/a/4403680/180275
#
#   Compare with exception_handling_unintended.py

try:
    int("y")
except (IndexError, ValueError):
    print "exception"
