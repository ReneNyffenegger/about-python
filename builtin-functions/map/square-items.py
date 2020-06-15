#!/usr/bin/python

nums    = [4, 9, 5, 2, 8]

#
#   Apply a lambda expression on each element of nums
#   to calculate the square of the number and return
#   the number and its square in a tuple:
#
for squared in map(lambda num: (num, num*num), nums):
    print(' {:d}^2 = {:2d}'.format(squared[0], squared[1]))
