class A:

      def __init__(self, num):
          print('A.__init__')
          self.num = num

      def method_a(self):
          print(f'A.method_a, num = {self.num}')

      def method_c(self):
          print('A.method_c')
      
      def method_d(self):
          print('A.method_d')

class B:

      def __init__(self, txt):
          print('B.__init__')
          self.txt = txt

      def method_b(self):
          print('B.method_b')

      def method_c(self):
          print('B.method_c')

      def method_d(self):
          print('B.method_d')

class CLS(A, B):

      def __init__(self, num, txt):
          print('CLS.__init__')

          A.__init__(self, num)
          B.__init__(self, txt)

      def method_d(self):
          print('CLS.method_d')

       #  A.method_d(self)
       #  B.method_d(self)

obj = CLS(42, 'Hello world')

obj.method_a()
obj.method_b()
obj.method_c()
obj.method_d()

print(isinstance(obj, A  )) # True
print(isinstance(obj, B  )) # True
print(isinstance(obj, CLS)) # True
