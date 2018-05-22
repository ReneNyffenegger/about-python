#!/usr/bin/python

import re

match = re.search('(\d\d\d|\w\w\w)', 'one 234 five s')
if match:
   print (match.group())
   # one
   print (match.group(1))
   # one
else:
   print ("didn't match")
