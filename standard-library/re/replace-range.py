#!/usr/bin/python
import re

txt = 'abc defghi jklmn opq rstu vwx yz';

print(re.sub('[g-p]', '*', txt))
#
#  abc def*** ***** **q rstu vwx yz
#
