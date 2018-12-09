#!/usr/bin/python3

def F2(a, *b):
    print ('in F2')
    print ('  a : ' + a)
    
    for b_ in b:
        print ('  b_: ' + b_)

F2('foo', 'bar', 'baz')
# in F2
#   a : foo
#   b_: bar
#   b_: baz

def F3(**p):
    print ('in F3')
    for k, v in p.iteritems():
        print ('  %-5s=%s' % (k, v) )

F3(one='foo', two='bar', three='baz')
# in F3
#   three=baz
#   two  =bar
#   one  =foo
