#!/usr/bin/python
import sys

f = open(__file__)
l1 = f.readline()
l2 = f.readline()
l3 = f.readline()
l4 = f.readline()

print(l4.rstrip('\n'))
print(l3.rstrip('\n'))
print(l2.rstrip('\n'))
print(l1.rstrip('\n'))
