import pandas
import numpy

df = pandas.DataFrame( {
        'c1'   : pandas.Series( ['foo','bar','baz',    'foo','bar','baz',    'bar',   'foo','foo'] ),
        'c2'   : pandas.Series( [  'X',  'Y',  'Z',      'X',  'Y',  'Z',      'X',     'Z',  'Z'] ),
        'vals' : pandas.Series( [  10 ,  20 ,  30 ,       1 ,   2 ,   3 ,      17 ,    100 ,  50 ] )
      })

piv = df.pivot_table(
            index  =['c1'  ], 
            columns=['c2'  ],
            values =['vals'],
            aggfunc=numpy.sum)

print type(piv)
# <class 'pandas.core.frame.DataFrame'>

print piv
#      vals
# c2      X   Y    Z
# c1
# bar    17  22  NaN
# baz   NaN NaN   33
# foo    11 NaN  150
