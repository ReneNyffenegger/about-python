#!/usr/bin/python

import re

re_numbers = re.compile('\d+')

for found in re_numbers.findall('foo 42 bar 18 baz 19 x'):
    print (found)
    # 42
    # 18
    # 19
