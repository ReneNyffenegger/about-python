#
#  https://www.youtube.com/watch?v=DnKxKFXB4NQ
#

from functools import cache

#
#  Try commenting @cache
#
@cache
def fib(n):
    if n <= 1:
       return 1

    return fib(n-1) + fib(n-2)

for i in range(400):
    print(i, fib(i))
