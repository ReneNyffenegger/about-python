class cls:

  def __init__(self, m1):
        self.m1 = m1

  def f(self, m2):
        print(f'm1: {self.m1}, m2: {m2}')


obj = cls(7)

obj_f = obj.f
cls_f = cls.f

print(type(obj_f))
#
#  <class 'method'>

print(type(cls_f))
#
#  <class 'function'>

print(obj_f.__self__  is obj  )
#
#  True

print(obj_f.__func__  is cls_f)
#
#  True

obj_f(4)
#
#  m1: 7, m2: 4
