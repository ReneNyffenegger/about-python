def Y():
    print ('yiedling foo')
    yield 'foo'

    print ('yielding bar')
    yield 'bar'

    print ('yielding baz')
    yield 'baz'


for y in Y():
    print ('y: ' + y)
    # yiedling foo
    # y: foo
    # yielding bar
    # y: bar
    # yielding baz
    # y: baz


def YY():
    for i in ['FOO', 'BAR', 'BAZ']:
        print ('yielding ' + i)
        yield i

for yy in YY():
    print ('yy: ' + yy)
    # yielding FOO
    # yy: FOO
    # yielding BAR
    # yy: BAR
    # yielding BAZ
    # yy: BAZ

def YYY():
    for i in [1, 2, 3, 4, 5, 6]:
        
        if i != 3:
           print ('yielding ' + str(i))
           yield i

        else:
           return


#   Note:
#     numbers 3 through 6 are not printed.
for yyy in YYY():
    print 'yyy: ' + str(yyy)
    # yielding 1
    # yyy: 1
    # yielding 2
    # yyy: 2
