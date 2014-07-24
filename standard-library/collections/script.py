#/usr/bin/python

import collections

cnt=collections.Counter()

for word in "foo bar baz more or less foo most foo even more foo or is it less".split():
    cnt[word]+=1

for word in cnt:
    print "%-10s: %d" % (word, cnt[word])
