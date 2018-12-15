#!/usr/bin/python3

class TQ84():

    class Nested():
        def __init__(self, name):
            self.name = name

        def __str__(self):
           return 'A.Nested, name = ' + self.name

n = TQ84.Nested('foo')
print(n)
#
# A.Nested, name = foo
