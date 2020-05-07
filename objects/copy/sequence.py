orig    = [1,2,3]

aliased = orig
copied  = orig[:]

orig.append(4)

print('elements in aliased:')
for x in aliased:
    print('  {}'.format(x))
#
# elements in aliased:
#   1
#   2
#   3
#   4

print('elements in copied:')
for x in copied:
    print('  {}'.format(x))
#
# elements in copied:
#   1
#   2
#   3
