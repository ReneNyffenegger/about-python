

a = ['foo', 'bar', 'baz']
b = ['one', 'two', 'three', 'four']



if any(word in ['hello', 'bar', 'world'] for word in a):
   print "yes"
else:
   print "no"

#  Yes

#  -----------------------------

if any(word in ['hello', 'bar', 'world'] for word in b):
   print "yes"
else:
   print "no"

#  No
