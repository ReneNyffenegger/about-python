#/usr/bin/python

import FooModule

print FooModule.module_func_sum (38, 4)  # 42
print FooModule.module_func_mult(21, 2)  # 42

print FooModule.BarModule.bar_func_4()

# print module_func_sum(38,4)            # NameError: name 'module_func_sum' is not defined
