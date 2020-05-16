def F(a, b, c):

    if a < b < c:
       print('{} < {} < {}'.format(a, b, c))

    if a < b > c:
       print('{} < {} > {}'.format(a, b, c))


F(10, 20, 30)
#
#  10 < 20 < 30

F(11, 22, 15)
#
#  11 < 22 > 15

F(10, 20,  5)
#
#  10 < 20 > 5
