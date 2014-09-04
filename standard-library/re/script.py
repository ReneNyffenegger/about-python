import re

re_number = re.compile('\d+')


for i in ['foo', 'bar 42 baz', 'hello', 'etc', '20' ]:

    if re_number.match(i):
       print i + " is a number"

    if re_number.search(i):
       print i + " contains a number"
