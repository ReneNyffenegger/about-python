#!/usr/bin/python3

def F_named_args(a, b, c = 'FOO', d = 'BAR', e = 'BAZ'):
    print(''               )
    print('  a = ' + str(a))
    print('  b = ' + str(b))
    print('  c = ' + str(c))
    print('  d = ' + str(d))
    print('  e = ' + str(e))

# --------------------------
#
#     Normal call
#
F_named_args('one', 'two')
#
#  a = one
#  b = two
#  c = FOO
#  d = BAR
#  e = BAZ

# -------------------------------
#
#     Explicitely pass a value for a
#     key-argument:
#
F_named_args('one', 'two', d='DDD')
#
#  a = one
#  b = two
#  c = FOO
#  d = DDD
#  e = BAZ

# -------------------------------
#
#     Positional arguments can
#     be named, too:
#
F_named_args(b='BBB', a='AAA')
#
#  a = AAA
#  b = BBB
#  c = FOO
#  d = BAR
#  e = BAZ
