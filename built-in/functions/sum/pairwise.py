x = [1, 5, 4]
y = [2, 4, 3]

p = sum(x*y for x,y in zip(x,y))

print(p)
