#!/usr/bin/python3

def two_stars(a, **b):
    print('')
    print('  a = ' + str(a))
    print('  type(b) = ' + str(type(b)))

    for k,v in b.items():
        print('  ' + k + ' = ' + str(v))

two_stars('foo')
#
#  a = foo
#  type(b) = <class 'dict'>
#

two_stars('bar', num = 42)
#
#  a = bar
#  type(b) = <class 'dict'>
#  num = 42

two_stars('baz', x = 'eggs', y = 'why')
#
#  a = baz
#  type(b) = <class 'dict'>
#  x = eggs
#  y = why
