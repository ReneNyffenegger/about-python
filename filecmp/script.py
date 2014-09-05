import filecmp

if filecmp.cmp('a.txt', 'b.txt'):
   print "a.txt == b.txt"
else:
   print "a.txt != b.txt"

  
if filecmp.cmp('a.txt', 'c.txt'):
   print "a.txt == c.txt"
else:
   print "a.txt != c.txt"
