lst = ['foo', 'bar', None, 'baz' ]

itr = iter(lst)

while elm := next(itr):
      print(elm)
