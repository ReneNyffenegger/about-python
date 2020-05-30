class desc:

  def __get__(self, obj, objtype):
      print('__get__ was called, obj.ident =', obj.ident)
      return self.val

  def __set__(self, obj, val):
      print('__set__ was called, obj.ident =', obj.ident)
      self.val = val

  def __delete__(self, obj):
      print('__delete__ was called, obj.ident =', obj.ident)


class CLS:
#
# Note: D (the descriptor object) is a class
# variable, not an instance variable:
#
  D = desc()

  def __init__(self, ident):
      self.ident = ident


obj_a = CLS('A')
obj_b = CLS('B')

obj_a.D = 42
#
#  __set__ was called, obj.ident = A(

obj_b.D = 99
#
#  __set__ was called, obj.ident = B

val_a = obj_a.D
#
#  __get__ was called, obj.ident = A

val_b = obj_b.D
#
#  __get__ was called, obj.ident = B

print(val_a)
#
#  99

print(val_b)
#
#  99

del obj_a.D
#
#  __delete__ was called, obj.ident = A
