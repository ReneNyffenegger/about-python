class cls:

      def __init__(self, ident):
          self.ident = ident

      def f1(self):
          print('f1 was called, ident = {}'.format(self.ident))

      def f2(self):
          print('f2 was called, ident = {}'.format(self.ident))


def callMethodByName(obj, name):
    method = getattr(obj, name)
    method()


obj_1 = cls('one')
obj_2 = cls('two')

callMethodByName(obj_1, 'f1') # f1 was called, ident = one
callMethodByName(obj_2, 'f2') # f2 was called, ident = two
