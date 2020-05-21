d1 = { 'A': 'one', 'B': 'two',              'D': 'four'}
d2 = {             'B': 'TWO', 'C':'THREE'             }

d1.update(d2)

for k, v in d1.items():
    print(f'{k} = {v}')
#
#  A = one
#  B = TWO
#  D = four
#  C = THREE
