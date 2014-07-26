import pandas

df = pandas.DataFrame(
      { 'col_1': pandas.Series( [  10 ,  20 ,  30 ] ),
        'col_2': pandas.Series( ['foo','bar','baz'] ),
        'col_3': pandas.Series( [  'X',  'Y',  'Z'] )
      })

print type(df)
# <class 'pandas.core.frame.DataFrame'>

print df
#    col_1 col_2 col_3
# 0     10   foo     X
# 1     20   bar     Y
# 2     30   baz     Z
