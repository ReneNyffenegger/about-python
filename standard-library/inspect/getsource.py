import inspect

def F(a):
    print(f'F says {a}')

print(inspect.getsource(F))
