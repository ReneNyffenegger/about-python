lst = ['foo', 'bar', None, 'baz' ]

itr = iter(lst)

while elem := next(itr):
      print(elem)
