def F(par_1, par_2, *posArgs, **namedArgs):

    print('par_1 : ', par_1)
    print('par_2 : ', par_2)

    for posArg in posArgs:
        print('posArg: ', posArg)

    for parName, argVal in namedArgs.items():
        print('{:6s}:  {}'.format(parName, argVal))

    print('')

F( 42, 'hello World')
F( 99, 'ninety-nine', 'foo', 'bar', 'baz')
F('A', 'B'          ,  x = 'eggs', y = 'why')
F('C', 'D'          , 'E', 'F', ltr = 'G')
