#!/usr/bin/python

import importlib.util

spec = importlib.util.spec_from_file_location('What is this argument for????', '../dir-module/FooModule.py')
foo  = importlib.util.module_from_spec(spec)

spec.loader.exec_module(foo)

foo.print_something()
