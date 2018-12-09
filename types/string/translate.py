#!/usr/bin/python3

str = 'Foo bar baz';

#
# Replace o with u
#
print(str.translate( str.maketrans( 'o' , 'u'  ))) # Fuu bar baz

#
# Replace o with u, b with p
#
print(str.translate( str.maketrans( 'ob', 'up' ))) # Fuu par paz

#
# Following line causes: ValueError: the first two maketrans arguments must have equal length
#
# print(str.translate( str.maketrans( 'obr', 'up' )))
