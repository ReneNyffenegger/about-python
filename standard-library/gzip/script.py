import gzip
import filecmp

gz_out = gzip.open(__file__ + '.gz', 'wb')
orig   = open(__file__, 'rb')
gz_out.writelines(orig)
gz_out.close()
orig.close()

# --

gz_in  = gzip.open(__file__ + '.gz', 'rb')
back   = open(__file__ + '.back', 'wb')
back.writelines(gz_in)
back.close()
gz_in.close()

# --

if filecmp.cmp(__file__ , __file__ + '.back'):
   print __file__ + " and " + __file__ + '.back' + " are equal"
else:
   print __file__ + " and " + __file__ + '.back' + " differ"
