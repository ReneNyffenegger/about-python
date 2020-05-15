grid = [
         [ x * y for x in range(1, 5)]  # <- Create a list with 4 elements, y is determined by the following list comprehension
                 for y in range(0, 3)   # <- Create 3 of the previous expression (which is a list of 4 elements)
       ]

print(grid)
#
#  [[0, 0, 0, 0], [1, 2, 3, 4], [2, 4, 6, 8]]
