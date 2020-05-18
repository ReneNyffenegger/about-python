class vector:

   def __init__(self, *c):
       self.c = c

   def __add__(self, other):
       return vector( *(s+o for s,o in zip(self.c, other.c)) )

   def __mul__(self, other):
       return vector( *(s*o for s,o in zip(self.c, other.c)) )

   def __repr__(self):
       return 'vector({})'.format(', '.join(str(x) for x in self.c))

p = vector(4, 5, 6)
q = vector(1, 4, 2)

r = p+q
print(r)
#
#  vector(5, 9, 8)

x = vector(4, 1, 6, 3, 3)
y = vector(2, 7, 1, 3, 2)

z = x*y
print(z)
#
#  vector(8, 7, 6, 9, 6)
