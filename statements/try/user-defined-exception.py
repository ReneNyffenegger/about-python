class SomethingIsWrong(BaseException):

      def __init__(self, reason):
          self.reason = reason

      def __str__(self):
          return self.reason


try:
   print('one')
   raise SomethingIsWrong('xyz')
   print('two')

except SomethingIsWrong as somethingWrong:
    print(f'Exception caught: {str(somethingWrong)}')

