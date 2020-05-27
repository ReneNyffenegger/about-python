def func(a, b, c):

    """ The purpose of this function is to demonstrate
        how sipmle testcases can be embedded itno
        a function's docstring

    >>> func(9, 21, 12)
    42
    """

    return a+b+c

def willFail(a, b, c):

    """ Testing this function will fail because '42'
        is intented to far. The output will be something
        like
          Expected:
                  42
          Got:
              42

    >>> func(9, 21, 12)
        42
    """

    return a+b+c

import doctest
doctest.testmod()
