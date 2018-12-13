#!/usr/bin/python3

def is_substring_contained_in_string(substring, string):
    if substring in string:
       print(substring + ' is a substring of ' + string)
    else:
       print(substring + ' is not a substring of ' + string)

is_substring_contained_in_string('foo', 'hello world')
# foo is not a substring of hello world

is_substring_contained_in_string('bar', 'for bar baz')
# bar is a substring of for bar baz

is_substring_contained_in_string('in' , 'wintertime' )
# in is a substring of wintertime
