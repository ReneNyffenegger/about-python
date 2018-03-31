import re

re_number = re.compile('\d+')


for i in ['foo', 'bar 42 baz', 'hello', 'etc', '20' ]:

    if re_number.match(i):
       print (i + " is a number")

    if re_number.search(i):
       print (i + " contains a number")
    
    # bar 42 baz contains a number
    # 20 is a number
    # 20 contains a number

print ("---")

re_numbers = re.compile('\d+')

for found in re_numbers.findall('foo 42 bar 18 baz 19 x'):
    print (found)
    # 42
    # 18
    # 19

print ("---")

if re.search('\d\d\d', 'one 234 five six'):
   print ("matched")
   # matched
else:
   print ("didn't match")

print ("---")

match = re.search('(\d\d\d|\w\w\w)', 'one 234 five s')
if match:
   print (match.group())
   # one
   print (match.group(1))
   # one

else:
   print ("didn't match")


print ("---")
match = re.search('foo:\s+(\d+),\s+bar:\s+(\d+)', 'hello foo:   42, bar:  1001xyz')
if match:
   print (match.group() )  # foo:   42, bar:  1001
   print (match.group(1))  # 42
   print (match.group(2))  # 1001


print ("---")

for found in re.findall(r'(\w+)\s+(\d+)', 'foo 42 bar 18 baz 19 x'):
    print (found[0] + ': ' + found[1])
    # foo: 42
    # bar: 18
    # baz: 19

print ("---")

print (re.sub(r'\d+', 'XX', 'foo 42 bar 18 baz 19 x'))
# foo XX bar XX baz XX x
