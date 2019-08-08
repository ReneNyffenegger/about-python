#!/usr/bin/python3

with open('iter.txt') as txt_file:
     for txt_line in txt_file:
         print (txt_line, end='') # use end='' to omit printing new-lines
