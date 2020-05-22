lst = [ 'one', 'two', 'three', 'four', 'five' ]
itr = iter(lst)

one = next(itr)
rst = list(itr)

print(one)
#
#  one

print(type(rst))
#
#  <class 'list'>

print(rst)
#
#  ['two', 'three', 'four', 'five']
