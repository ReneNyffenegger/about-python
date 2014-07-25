#!/usr/bin/python

from FooModule import module_func_sum

print module_func_sum (38,4)                  # 42

# print FooModule.module_func_mult (38,4)     # NameError: name 'FooModule' is not defined
# print module_func_mult(21,2)                # NameError: name 'module_func_mult' is not define
