N = 'baz'
L = ['foo','bar']

def F(val = N, lst = L):
    lst.append(val)

N = 'xyz'

#
#  The following call appends 'baz', not 'xyz' to L:
#
F()

print(L)
#
# ['foo', 'bar', 'baz']

F('abc')
print(L)
#
# ['foo', 'bar', 'baz', 'abc'] 

anotherList = ['a', 'b', 'c']
F(val = 'd', lst = anotherList)

print(L)
#
# ['foo', 'bar', 'baz', 'abc']

print(anotherList)
#
#  ['a', 'b', 'c', 'd']
