class A: pass
class B: pass

class C(A, B): pass

print(A.__mro__)
#
#  (<class '__main__.A'>, <class 'object'>)

print(B.__mro__)
#
#  (<class '__main__.B'>, <class 'object'>)

print(C.__mro__)
#
#  (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

a = A()
b = B()
c = C()

assert not hasattr(a, '__mro__')
assert not hasattr(b, '__mro__')
assert not hasattr(c, '__mro__')
