def F(p1, p2):

    var = 'baz'

    sym = locals()
    for k, v in sym.items():
        print('{:3s} = {:20}'.format(k,v))

F('foo', 'bar')
