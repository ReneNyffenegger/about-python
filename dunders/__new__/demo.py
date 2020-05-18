class META(type):

      def __new__(cls, name, bases, body):

          print(f'  __new__'                         )
          print(f'    cls.__name__  = {cls.__name__}') # META
          print(f'    name          = {name        }') # BASE

          for k, v in body.items():
              print('    item[{!r}] = {!r}'.format(k, v))

          x = super().__new__(cls, name, bases, body)

          return x


print('Going to define/create a class:')

class BASE(metaclass=META):

      def __init__(self):
          print('  __init__')
          print('    id(self) = {}'.format(id(self)))
          print('    id(self.class) = {}'.format(id(self.__class__)))

      def f1(self):
          print('BASE.f1')

      def f2(self):
          print('BASE.f2')

print('Finished with the creation of the class')

b1 = BASE()
b2 = BASE()
