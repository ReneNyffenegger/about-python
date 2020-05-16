someList = ['foo', 'bar', 'baz']

enumeratedList = enumerate(someList)

print (type(enumeratedList))
# <class 'enumerate'>

for index, element in enumeratedList:
    print("{:d}: {:s}".format(index, element) )
# 0: foo
# 1: bar
# 2: baz
