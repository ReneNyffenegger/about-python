def TQ84_decorator(func):

    print(f'TQ84_decorator was called for func {func.__name__}')

    def newFunc(*a, **kw):
        print(f'newFunc is calling {func.__name__}')
        func(*a, **kw)

    return newFunc


print('defining funcOne')

@TQ84_decorator
def funcOne():
    print(f'Within FuncOne')

print('defining funcTwo')

@TQ84_decorator
def funcTwo(p):
    print(f'Within FuncTwo, p = {p}')

print('calling  funcOne:')
funcOne()

print('calling  funcTwo:')
funcTwo(99)
