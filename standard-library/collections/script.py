#/usr/bin/python

import collections

cnt=collections.Counter()

for word in "foo bar baz more or less foo most foo even more foo or is it less".split():
    cnt[word]+=1

print "for word in cnt"
for word in cnt:
    print "  %-10s: %d" % (word, cnt[word])

print "\nfor word in cnt.most_common(3)"
for word in cnt.most_common(3):
    print "  %-10s: %d" % word
