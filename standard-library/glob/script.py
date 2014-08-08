import os
import sys
import glob

if len(sys.argv) < 3:

   print
   print "Usage       ", sys.argv[0], " dir suffix"
   print 'For example ', sys.argv[0], ' c:\\temp txt'
   exit

dir_   = sys.argv[1]
suffix = sys.argv[2]

os.chdir (dir_)

matched_files = glob.glob("*." + suffix)

print "\n".join(matched_files)
