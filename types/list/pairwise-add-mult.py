lst_1 = [3, 7, 5]
lst_2 = [4, 2, 1]

lst_a = [ x+y for x, y in zip(lst_1, lst_2) ]
lst_m = [ x*y for x, y in zip(lst_1, lst_2) ]

print(lst_a)
#
#  [7, 9, 6]

print(lst_m)
#
#  [12, 14, 5]
