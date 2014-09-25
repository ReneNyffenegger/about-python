def starts_with_b(t):
    return t[0] == 'b'
    

a = ['foo', 'bar', 'baz']

print filter(starts_with_b, a)
# ['bar', 'baz']

print filter(lambda t: t[0] == 'b', a)
# ['bar', 'baz']

print filter(None, [0, 'foo', None, 'bar', 'baz']) # Note: 0 and None will be gone...
# ['foo', 'bar', 'baz']
