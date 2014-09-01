a = ['foo', 'bar', 'baz']



if all(word in ['foo', 'bar'] for word in a):
   print "yes"
else:
   print "no"

#  no

#  -----------------------------

if all(word in ['foo', 'bar', 'baz'] for word in a):
   print "yes"
else:
   print "no"

#  yes

#  -----------------------------

if all(word in ['foo', 'bar', 'baz', 'loch-ness'] for word in a):
   print "yes"
else:
   print "no"
   
#  yes
