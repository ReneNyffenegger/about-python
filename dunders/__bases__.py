class A            : pass
class B            : pass
class C            : pass
class D            : pass

class ABD(A, B, D ): pass
class BC (B, C    ): pass

class x(ABD, BC   ): pass

print([ _.__name__ for _ in   x.__bases__])
#
#   ['ABD', 'BC']

print([ _.__name__ for _ in ABD.__bases__])
#
#   ['A', 'B', 'D']

print([ _.__name__ for _ in   x.__mro__  ])
#
#   ['x', 'ABD', 'A', 'BC', 'B', 'D', 'C', 'object']
