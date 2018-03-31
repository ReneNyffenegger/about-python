import re

txt = 'abc, def, ghi'

x=re.split(', *', txt)
for y in x:
    print(y)

