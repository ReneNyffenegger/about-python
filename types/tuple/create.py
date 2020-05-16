empty_tuple            = ()
tuple_with_one_element = 'one',  # note the trailing comma
tup_1_2                =  1, 2
tup_X                  =  1, 2,  # another trailing comma

for t in [ empty_tuple, tuple_with_one_element, tup_1_2, tup_X]:
    if not isinstance(t, tuple):
       print('wrong assumption for', str(t), ', type is', type(t))
