#!/usr/bin/python

import re

if re.search('\d\d\d', 'one 234 five six'):
   print ("matched")
   # matched
else:
   print ("didn't match")
