class class_with_dir:

      def __dir__(self):
          return ['one', 'two', 'three']

      def __getattr__(self, name):
          if name == 'one'  : return 1
          if name == 'two'  : return 2
          if name == 'three': return 3



obj_1 = class_with_dir()
print(dir(obj_1))
#
#  ['one', 'three', 'two']

print(obj_1.two)
#
#  2


class class_with_dict:

      def __init__(self):
          self.__dict__ = {'one'  : 1,
                           'two'  : 2,
                           'three': 3}

obj_2 = class_with_dict()

print(dir(obj_2))
#
# ['__class__', '__delattr__', … 'one', 'three', 'two']

print(obj_2.three)
#
#  3

class class_with_both:

      def __init__(self):
          self.__dict__ = {'foo': 'F',
                           'bar': 'G',
                           'baz': 'H'}

      def __dir__(self):
          return ['A', 'B', 'C']

obj_3 = class_with_both()
print(dir(obj_3))
#
#  ['A', 'B', 'C']
