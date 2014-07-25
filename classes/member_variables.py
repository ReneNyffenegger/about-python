#!/usr/bin/python


class A(object):

  
  def __init__(self, ident):

      self.ident = ident
      foo        ='local variable'

  def go(self):
      
      print ("go " + self.ident)
#     print foo

a = A('aaa')

print a.ident    # aaa

# print a.foo    # AttributeError: 'A' object has no attribute 'foo'
# print foo      # NameError: name 'foo' is not defined

a.go()           # go aaa
