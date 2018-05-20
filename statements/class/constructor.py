#!/usr/bin/python

class ABC:

    def __init__(self, x, y):
    #
    #   The class's constructor.
    #   The first parameter is automatically aliased
    #   to the instance being constructed.
    #
        print('Constructor being executed')
        self.x = x
        self.y = y

    def show(self):
        print('x = {:d}, y = {:s}'.format(self.x, self.y))


#
#   Initialize an instance of a class.
#   Note: there is no 'new' statement, using
#   the class name with following paranthesis
#   is sufficient.
#
abc = ABC(42, 'foo')
abc.show()
