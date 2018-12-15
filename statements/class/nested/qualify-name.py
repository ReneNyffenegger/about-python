#!/usr/bin/python3

class CLS():

    class Nested():
        def __init__(self, name):
            self.name = name

        def __str__(self):
            return 'CLS.Nested, name = ' + self.name

    def __init__(self, name, name_nested):
        self.name = name
     #
     #  Note: Even though B.Nested is nested within
     #  class B, Nested needs to be qualified with
     #  either self.Nested or B.Nested!
     #
        self.nested = CLS.Nested(name_nested)

    def __str__(self):
        return 'CLS, name = ' + self.name + ' - ' + str(self.nested)

inst = CLS('bar', 'baz')
print(inst)
#
# CLS, name = bar - CLS.Nested, name = baz
