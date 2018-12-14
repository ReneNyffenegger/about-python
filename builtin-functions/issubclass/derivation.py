#!/usr/bin/python3

class A():
    pass

class B(A):
    pass

class C(B):
    pass

if issubclass(A, B):
   print('A is a subclass of B')
else:
   print('A is not a subclass of B')

if issubclass(B, A):
   print('B is a subclass of A')
else:
   print('B is not a subclass of A')

if issubclass(C, A):
   print('C is a subclass of A')
else:
   print('C is not a subclass of A')
#
# A is not a subclass of B
# B is a subclass of A
# C is a subclass of A
