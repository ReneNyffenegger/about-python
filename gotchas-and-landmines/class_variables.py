#
#     http://stackoverflow.com/a/531327/180275
#

class AAA(object):
      x = 1

class BBB(AAA):
      pass

class CCC(BBB):
      pass


print AAA.x, BBB.x, CCC.x   # 1 1 1

BBB.x = 2

print AAA.x, BBB.x, CCC.x   # 1 2 2

AAA.x = 3

print AAA.x, BBB.x, CCC.x   # 3 2 2

a = AAA()

print a.x, AAA.x            # 3 3

a.x = 4

print a.x, AAA.x            # 4 3
