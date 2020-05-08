class class_with_reversed:

      def __reversed__(self):

          yield 'I'
          yield 'say'
          yield 'hello'
          yield 'world'


obj = class_with_reversed()

for e in reversed(obj):
    print(e)
#
#  I
#  say
#  hello
#  world
