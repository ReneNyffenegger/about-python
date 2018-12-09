#!/usr/bin/python3

txt = 'Foo bar baz'

print(txt.replace('o' , 'u' )) # Fuu bar baz
print(txt.replace('a' , 'AA')) # Foo bAAr bAAz
print(txt.replace('ar', 'XY')) # Foo bXY baz
