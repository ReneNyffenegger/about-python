items = [ 'foo', 'baz', 'foo', 'bar', 'foo', 'baz', 'baz', 'bar', 'foo', 'baz' ]

try:

  ix = 0
  while True:
    ix = items.index('foo', ix)
    print(f'found foo at position {ix}')
    ix += 1

except ValueError:
   pass
