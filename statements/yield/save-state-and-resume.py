def func(init_val):

    local_var = init_val
    print(f'yielding {local_var}')
    yield local_var

    local_var += 5
    print(f'yielding {local_var}')
    yield local_var

    local_var *= 2
    print(f'yielding {local_var}')
    yield local_var

    print('the end.')

gen = func(17)

try:
    # gen.__iter__()
    print(f'__next()__ returned: {gen.__next__()}')
    print(f'__next()__ returned: {gen.__next__()}')
    print(f'__next()__ returned: {gen.__next__()}')
    print(f'__next()__ returned: {gen.__next__()}')
except StopIteration:
    print('Caught StopIteration')

print('--------------------------------------')

gen = func(5)
itr = iter(gen)

try:
    print(f'next(itr) = {next(itr)}')
    print(f'next(itr) = {next(itr)}')
    print(f'next(itr) = {next(itr)}')
    print(f'next(itr) = {next(itr)}')

except StopIteration:
    print('Caught StopIteration')
