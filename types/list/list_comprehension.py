# -*- coding: utf-8 -*-

squares = [i**2 for i in range(11)] # compare with « map(lambda i: i**2, range(11)) »
print squares
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


squares_of_even_numbers = [i**2 for i in range(11) if i % 2 ==0]
print squares_of_even_numbers
# [0, 4, 16, 36, 64, 100]
