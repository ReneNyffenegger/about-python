from functools import partial

def F(p1 = 'one', p2 = 'two', p3 = 'three', p4='four', p5='five'):
    print(f'p1: {p1}')
    print(f'p2: {p2}')
    print(f'p3: {p3}')
    print(f'p4: {p4}')
    print(f'p5: {p5}')


f = partial(F, 'A', 'B', p4 = 'Y', p5 = 'Z')

assert f.func is F

print (f.args    )
#
#   ('A', 'B')

print (f.keywords)
#
#   {'p4': 'Y', 'p5': 'Z'}


f('C')
#
#  p1: A
#  p2: B
#  p3: C
#  p4: Y
#  p5: Z

f(p4 = 'y')
#
#  p1: A
#  p2: B
#  p3: three
#  p4: y
#  p5: Z
