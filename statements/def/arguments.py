#!/usr/bin/python3

def F_args(a, b, c):
    print(''               )
    print('  a = ' + str(a))
    print('  b = ' + str(b))
    print('  c = ' + str(c))

F_args('foo', 'bar', 'baz')
#
#  a = foo
#  b = bar
#  c = baz

# Any type can be passed to the function …
# … but in order to print them, the function
# needs to call str()
F_args(   1 ,    2 ,    3 )
#
#  a = 1
#  b = 2
#  c = 3
