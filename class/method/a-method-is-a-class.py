class cls:

      def __init__(self, ident):
          self.ident = ident

      def x(self):
          print('x was called, ident = {}'.format(self.ident))

      def y(self):
          print('y was called, ident = {}'.format(self.ident))


obj_1 = cls('foo')
obj_2 = cls('bar')

m1 = obj_1.x
m2 = obj_2.y

m1()
#
#  x was called, ident = foo

m2()
#
#  y was called, ident = bar

print(type(m1))
#
#  <class 'method'>

