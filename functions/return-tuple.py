def F():

    return 42, 99, -1


x, y, z = F()

print('x={}, y={}, z={}'.format(x, y, z))
#
# x=42, y=99, z=-1

t = F()
print('type(t) = {}'.format(type(t)))
#
# type(t) = <class 'tuple'>

print('t[0]={}, t[1]={}, t[2]={}'.format(t[0], t[1], t[2]))
#
# t[0]=42, t[1]=99, t[2]=-1

# (a, rest) = F() # -->  ValueError: too many values to unpack (expected 2)
