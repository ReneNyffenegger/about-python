#!/usr/bin/python3

def one_star(a, *b):
    print('')
    print('  a = ' + str(a))
    print('  type(b) = ' + str(type(b)))
    for b_ in b:
        print('  b_= ' + str(b_))

one_star('foo')
#
#  a = foo
#  type(b) = <class 'tuple'>

one_star('bar', 'baz')
#
#  a = bar
#  type(b) = <class 'tuple'>
#  b_= baz

one_star('one', 'two', 'three')
#
#  a = one
#  type(b) = <class 'tuple'>
#  b_= two
#  b_= three

# one_star(a = 'a', b='b', c='c') # --> TypeError: one_star() got an unexpected keyword argument 'b'
