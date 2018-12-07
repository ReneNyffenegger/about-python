#!/usr/bin/python3

#
#  Creating a dictionary
#
d = {'one'   : 1,
     'two'   : 2,
     'three' : 3}

#
#  Adding more items to the dictionary
#
d['four'] = 4
d['five'] = 5

for k,v in d.items():
    print(k, ' = ', v)
