import pandas

df = pandas.DataFrame(
      { 'col_1': pandas.Series( [  10 , None,  30  , None ] ),
        'col_2': pandas.Series( [  'X',  'Y',  'Z' ,  'Q' ] )
      })


df.col_1 = df.col_1.fillna( 999 )

print df
#    col_1 col_2
# 0     10     X
# 1    999     Y
# 2     30     Z
# 3    999     Q
