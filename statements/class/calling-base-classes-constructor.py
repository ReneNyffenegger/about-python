#!/usr/bin/python


class A:
  def __init__(self):
      print("  A's constructor")


class B(A):

  def __init__(self):
  #   Call A's constructor:
      A.__init__(self)
      print("  B's constructor")
        

class C(A):

  def __init__(self):
  #   Note: A's constructor is not called
      print("  C's constructor")

print('Creating a B')
b = B()

print('Creating a C')
c = C()
