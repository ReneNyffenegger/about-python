a      =  [ 'one', 'two', 'three', 'four' ]

# Make a copy of a. Note: not a deep copy because references within
# point to the same object.
a_copy = a[:]

# Create a reference to the array pointed at by 'a'.
a_ref  = a

a_copy.append('five')
a_ref .append('FIVE')

print(a_copy) # ['one', 'two', 'three', 'four', 'five']
print(a_ref ) # ['one', 'two', 'three', 'four', 'FIVE']
print(a     ) # ['one', 'two', 'three', 'four', 'FIVE']
