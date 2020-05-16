d = { word: len(word) for word in ['one', 'two', 'three', 'four', 'five', 'six'] }

for k, v in d.items():
    print('{:5s}: {}'.format(k, v))
#
#  one  : 3
#  two  : 3
#  three: 5
#  four : 4
#  five : 4
#  six  : 3
