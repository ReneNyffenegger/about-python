#
#    http://stackoverflow.com/a/530577/180275
#

some_list       = ['foo', 'bar', 'baz'  ]
some_other_list = ['one', 'two', 'three']

print "some_list"
for item in some_list:
    print item

#   foo
#   bar
#   baz

print "some_other_list"
for iten in some_other_list:  # note the typo: "iten" instead of "item"
    print item

#   baz
#   baz
#   baz
