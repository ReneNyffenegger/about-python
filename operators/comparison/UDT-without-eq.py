#!/usr/bin/python3

class C:
    def __init__(self, a, b):
        self.a = a
        self.b = b


c1 = C(5, 3)
c2 = C(5, 3)
c3 = C(1, 9)

if c1 == c2:
   print('c1 == c2')
else:
   print('c1 != c2')
# c1 != c2

if c1 == c3:
   print('c1 == c3')
else:
   print('c1 != c3')
# c1 != c3
