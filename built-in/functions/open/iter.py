#!/usr/bin/python3

with open('iter.txt') as txt:
     for line in iter(txt.readline, ''):
       # Remove trailing new line because…
         line = line.rstrip('\n')
       # … it is implicitely added in print()
         print(line)
