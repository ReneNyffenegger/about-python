
def callMultiple(howMany):

    print(f'callMultiple({howMany})')

    def decorator(func):

        print(f'  decorator({func.__name__})')

        def caller(*a, **kw):
            print('   caller')
            for n in range(howMany):
                print(f'      n = {n}')
                func(*a, *kw) 

        return caller

    print('returning decorator')
    return decorator


print('Defining F')

@callMultiple(5)
def F(x):
    print(f'F: x = {x}')

print('Calling F')
F('foo')
