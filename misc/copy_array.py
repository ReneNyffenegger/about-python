a      =  [ 'one', 'two', 'three', 'four' ]
a_copy = a[:]
a_ref  = a

a_copy.append('five')
a_ref .append('FIVE')

print(a_copy) # ['one', 'two', 'three', 'four', 'five']
print(a_ref ) # ['one', 'two', 'three', 'four', 'FIVE']
print(a     ) # ['one', 'two', 'three', 'four', 'FIVE']
