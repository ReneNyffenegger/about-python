from collections import deque

D = deque([ 'one', 'two', 'three', 'four' ])
D.append('five')
D.append([ 'six', 'seven' ])

print(D.popleft()) # one
print(D.popleft()) # two

print(D) # deque(['three', 'four', 'five', ['six', 'seven']])
