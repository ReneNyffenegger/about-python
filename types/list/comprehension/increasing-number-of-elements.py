a = [ [R  for L in range(0,R) ]
          for R in range(1,6) ]

print(a)
#
#  [[1], [2, 2], [3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5, 5]]

b = [ [L  for L in range(1,R) ]
          for R in range(2,7) ]
print(b)
#
#  [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]]
