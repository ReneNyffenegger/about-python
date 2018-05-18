#!/usr/bin/python

str="hello world, the famous number is forty-two, is it not?"

print('str.split()')
for word in str.split():
    print('  ' + word)

#  hello
#  world,
#  the
#  famous
#  number
#  is
#  forty-two,
#  is
#  it
#  not?

print("str.split(',')")
for part in str.split(','):
    print('  ' + part)

#  hello world
#   the famous number is forty-two
#   is it not?
