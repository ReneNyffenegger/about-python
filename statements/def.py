#!/usr/bin/python3

def F1(a = 'foo', b='bar', c='baz'):
    print ('in F1')
    print ('  a=' + a)
    print ('  b=' + b)
    print ('  c=' + c)

F1('one', 'two')
# in F1
#   a=one
#   b=two
#   c=baz

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
