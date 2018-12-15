#!/usr/bin/python3

numbers = [ 1   ,  2   ,  3                     ]
letters = ['a'  , 'b'  , 'c'    , 'd'   , 'e'   ]
words   = ['one', 'two', 'three', 'four'        ]

zipped = zip(numbers, letters, words)
for triple in zipped:
    print(triple)
#
# (1, 'a', 'one')
# (2, 'b', 'two')
# (3, 'c', 'three')
