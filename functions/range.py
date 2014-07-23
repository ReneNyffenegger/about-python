print range(   7)     # [0, 1, 2, 3, 4, 5, 6]
print range(3, 7)     # [3, 4, 5, 6]

#  TypeError: range() integer step argument expected, got float.
#  print range(5, 7, 0.333) 

print [ x * 0.333 for x in range(5 * 3, 7 * 3) ]  # [4.995, 5.328, 5.6610000000000005, 5.994000000000001, 6.327, 6.66]
