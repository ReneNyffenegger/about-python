def F(par, num = 42, txt='Hello world'):
    print('par = {}'.format(par))
    print('num = {}'.format(num))
    print('txt = {}'.format(txt))
    print('')

F('foo')
#
# par = foo
# num = 42
# txt = Hello world

F('bar', 99)
#
# par = bar
# num = 99
# txt = Hello world

F('baz',  3, 'good bye')
#
# par = baz
# num = 3
# txt = good bye

F('baz',  txt='abcdef')
#
# par = baz
# num = 42
# txt = abcdef
