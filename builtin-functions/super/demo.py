class A:

      def __init__(self, val):
          self.val = val

      def xyz(self):
          print('A.val = {}'.format(self.val))

class B(A):

      def __init__(self, val, txt):
          super().__init__(val)
          self.txt = txt

      def xyz(self):
          super().xyz()
          print('B.txt = {}'.format(self.txt))


a = A(11)
a.xyz()

b = B(42, 'hello world')
b.xyz()
