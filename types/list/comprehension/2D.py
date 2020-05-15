grid = [
         [ x * y for x in range(1, 5)]  # <- Create lists with 4 elements
                 for y in range(0, 3)   # <- Create lists with 3 elements
       ]

print(grid)
#
#  [[0, 0, 0, 0], [1, 2, 3, 4], [2, 4, 6, 8]]
