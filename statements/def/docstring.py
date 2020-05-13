def F():
    'This is the functions docstring'
    return 4


def G(a):
    """\
This docstring demonstrates that
a docstring can also span
multiple lines."""

    return a ** 2

print(F.__doc__)
print(G.__doc__)
