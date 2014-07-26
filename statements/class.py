#!/usr/bin/python


class A:

  def __init__(self):
      
      print "A's constructor"


class B(A):

  def __init__(self):

      A.__init__(self)          # Call A's constructor
      print "B's constructor"
        

class C(A):

  def __init__(self):
                                # Note: A's constructor is not called
      print "C's constructor"

b = B()
c = C()
