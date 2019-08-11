#!/usr/bin/python3

#
#   Open a file for reading
#
f = open('file.txt')

#
#   Skip a line
#
next(f)

#
#   Print the remaining lines
#
for l in f:
    print(l, end='')
