a = ['foo', 'bar', 'baz']


enum_a = enumerate(a)

print (enum_a)
# <enumerate object at 0x0139BE18>


for i, t in enum_a:
    print("%d %s" % (i, t) )
    # 0 foo
    # 1 bar
    # 2 baz
