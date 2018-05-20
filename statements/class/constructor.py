#!/usr/bin/python

class ABC:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print('x = {:d}, y = {:s}'.format(self.x, self.y))


abc = ABC(42, 'foo')
abc.show()
