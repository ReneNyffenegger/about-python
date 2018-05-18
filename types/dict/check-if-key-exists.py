#!/usr/bin/python

d = {'foo': 'abc', 'baz': 'def'}

for k in ['foo', 'bar', 'baz']:
    if k in d:
       print('Key {:s} exists, val is {:s}'.format(k, d[k]))
    else:
       print('Key {:s} does not exist'.format(k))
