from collections import deque

D = deque([ 'one', 'two', 'three', 'four' ])

#
#   Add items on the deque's right side:
#
D.append('five')

#
#   Add another item (which happens to be a list):
#
D.append([ 'six', 'seven' ])

#
# Add an on the deque's left side:
#
D.appendleft('zero')

print(D)
#
#  deque(['zero', 'one', 'two', 'three', 'four', 'five', ['six', 'seven']])


#
# Remove items on the right side
#
print(D.pop())     # ['six', 'seven']
print(D.pop())     #  five

#
# Remove an item on the left side
#
print(D.popleft()) # zero

print(D)           #  deque(['one', 'two', 'three', 'four'])
