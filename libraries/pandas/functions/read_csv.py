import pandas

data_frame = pandas.read_csv("data.csv")

print(type(data_frame)) # <class 'pandas.core.frame.DataFrame'>

print(data_frame)
#   col_1  col_2  col_3
# 0   foo    one      1
# 1   bar    two      2
# 2   baz  three      3
