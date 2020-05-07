class Cls:

    class notAvailableMember:
          def __init__(self, txt):
              self.txt = txt

          def __str__(self):
              return self.txt + ', which is unimplemented, was accessed as a member property'

          def __call__(self):
              print(self.txt + ', which is unimplemented, was called as a method')

    def __init__(self):
        self.member_one = 'first member'
        self.member_two = 'second member'

    def __getattr__(self, name):
        print('C.__getattr__ with name = ' + name + ' was called')

        return  Cls.notAvailableMember(name)

    def method_one(self):
        print('method_one was called')


c = Cls()

print(str(c.member_one  ))
#
#  first member

print(str(c.member_two  ))
#
#  second member

print(str(c.member_three))
#
#  C.__getattr__ with name = member_three was called
#  member_three, which is unimplemented, was accessed as a member property

c.method_one()
#
#  method_one was called

c.method_two()
#
#  C.__getattr__ with name = method_two was called
#  method_two, which is unimplemented, was called as a method
