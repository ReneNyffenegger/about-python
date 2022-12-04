import re

if match := re.search('foo:\s+(\d+),\s+bar:\s+(\d+)', 'hello foo:   42, bar:  1001xyz'):

   print (match.group() )  # foo:   42, bar:  1001
   print (match.group(1))  # 42
   print (match.group(2))  # 1001
