import pandas

q =  pandas.qcut ( [ 1, 2, 2, 4, 5, 9, 10, 12, 15, 16, 16, 18, 20, 23 ], 4)

print type(q)
# <class 'pandas.core.categorical.Categorical'>

print q
#   [1, 4.25]
#   [1, 4.25]
#   [1, 4.25]
#   [1, 4.25]
#  (4.25, 11]
#  (4.25, 11]
#  (4.25, 11]
#    (11, 16]
#    (11, 16]
#    (11, 16]
#    (11, 16]
#    (16, 23]
#    (16, 23]
#    (16, 23]
