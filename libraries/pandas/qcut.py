import pandas

q =  pandas.qcut ( [ 1, 2, 2, 4, 5, 9, 10, 12, 15, 16, 16, 18, 20, 23 ], 4)

print(type(q))
# <class 'pandas.core.arrays.categorical.Categorical'>

print(q)
#
# Length: 14
# Categories (4, interval[float64, right]): [(0.999, 4.25] < (4.25, 11.0] < (11.0, 16.0] <
#                                           (16.0, 23.0]]
