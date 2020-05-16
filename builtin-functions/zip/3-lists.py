numbers = [ 1   ,  2   ,  3     ,  4    ,  5    ]
letters = ['a'  , 'b'  , 'c'    , 'd'   , 'e'   ]
words   = ['one', 'two', 'three', 'four', 'five']

zipped = zip(numbers, letters, words)
for triple in zipped:
    print(triple)
#
# (1, 'a', 'one')
# (2, 'b', 'two')
# (3, 'c', 'three')
# (4, 'd', 'four')
# (5, 'e', 'five')
