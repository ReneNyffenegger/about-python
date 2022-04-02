import pandas

a = pandas.Series( [  42 , -11 ,  19 ])
b = pandas.Series( ['foo','bar','baz'])

print(type (a)) # <class 'pandas.core.series.Series'>

print(a)
# 0    42
# 1   -11
# 2    19

print(b)
# 0    foo
# 1    bar
# 2    baz