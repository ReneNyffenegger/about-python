orig = {
  'foo' :  1,
  'bar' :  7,
  'baz' :  9
}

aliased = orig
copied  = orig.copy()

orig['foo'] = 42
orig['baz'] = 99
orig['bar'] = -1


print('Key value pairs in aliased:')
for k, v in aliased.items():
    print('  {} = {}'.format(k,v))
#
#  Key value pairs in aliased:
#  foo = 42
#  bar = -1
#  baz = 99

print('Key value pairs in copied:')
for k, v in copied.items():
    print('  {} = {}'.format(k,v))
#
# Key value pairs in copied:
#   foo = 1
#   bar = 7
#   baz = 9
