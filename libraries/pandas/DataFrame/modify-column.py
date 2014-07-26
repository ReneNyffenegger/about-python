import pandas

df = pandas.DataFrame(
      { 'col_1': pandas.Series( [  10 ,  20 ,  30 ] ),
        'col_2': pandas.Series( ['foo','bar','baz'] ),
        'col_3': pandas.Series( [  'X',  'Y',  'Z'] )
      })


df.col_1 = df.col_1.map(lambda n: n * n)

print df
#    col_1 col_2 col_3
# 0    100   foo     X
# 1    400   bar     Y
# 2    900   baz     Z
