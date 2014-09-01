import numpy
import pandas

print numpy.mean( [ 10, 20, 30, 40, 1000] )
#  220.0


df = pandas.DataFrame(
      { 'col_1': pandas.Series( [  10 ,  20 ,  30 ,  40 ] ),
        'col_2': pandas.Series( ['foo','bar','baz','qux'] ),
        'col_3': pandas.Series( [  'X',  'Y',  'Z',  'Q'] )
      })

print numpy.mean(df.col_1)
# 25.0
