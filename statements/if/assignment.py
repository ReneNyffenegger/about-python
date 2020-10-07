def half(n):

    r = n/2
    return r if int(r) == r else None


def F(n):

    if h := half(n):
       print('half({}) = {}'.format(n,h))
    else:
       print('{} is odd'.format(n))


F(42)
F(99)
