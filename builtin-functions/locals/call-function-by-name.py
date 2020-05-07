def F1(a, b):
    print('{} + {} = {}'.format(a, b, a+b))

def F2(a, b):
    print('{} - {} = {}'.format(a, b, a-b))

def F3(a, b):
    print('{} * {} = {}'.format(a, b, a*b))

def F4(a, b):
    print('{} / {} = {}'.format(a, b, a/b))


for nr in range(1, 5):
    locals()['F' + str(nr)](42, 6)
#
#  42 + 6 = 48
#  42 - 6 = 36
#  42 * 6 = 252
#  42 / 6 = 7.0
