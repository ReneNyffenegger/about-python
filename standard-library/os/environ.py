import os
import sys

print("Defined environment variables:")
for var in os.environ:
    if var == 'PATH':
       sys.stdout.write ("  %-25s = " % var)
       path_iter = iter(sys.path)
       print(next(path_iter))  # print 1st path on same line as "PATH...="
       for dir in path_iter:   # print other paths indented:
           print((' ' * 30) + dir)
    else:
       print("  %-25s = %s  " % (var, os.environ[var]))

print('')
print("Expanded $HOME")
print("  " + os.path.expandvars('$HOME'))
