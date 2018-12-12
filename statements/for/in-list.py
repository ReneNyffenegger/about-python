#!/usr/bin/python3

lst = ['foo', 'bar', 'baz']

for elm in lst:
 #  elm is not aliased to the element in the list.
 #  Thus, the following statement does not change the
 #  list:
    elm += '!'
    print(elm)


  # checking assertion that list
  # was not changed by the += operater:
for elm in lst:
    print(elm)
