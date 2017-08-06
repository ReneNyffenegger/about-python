import copy

array_123 = [   1 ,    2 ,    3 ]
array_fbb = ['foo', 'bar', 'baz']

array_of_arrays = [ 'array of arrays', array_123, array_fbb ]

array_of_arrays_ref      =               array_of_arrays
array_of_arrays_copy     =               array_of_arrays[:]
array_of_arrays_deepcopy = copy.deepcopy(array_of_arrays)

# ----------------------------------------------------
#
array_of_arrays[0] = 'Changed'

print(array_of_arrays_ref     [0]) # Changed
print(array_of_arrays_copy    [0]) # array of arrays
print(array_of_arrays_deepcopy[0]) # array of arrays

array_of_arrays[2][0] = 'Changed foo'

print(array_of_arrays_ref     [2][0]) # Changed foo
print(array_of_arrays_copy    [2][0]) # Changed foo
print(array_of_arrays_deepcopy[2][0]) # foo
