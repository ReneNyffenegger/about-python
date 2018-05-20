#!/usr/bin/python

import textwrap


def print_string():
 #
 #  Note the backslash!
 #
    print(textwrap.dedent('''\
        There was a foo, and
        a bar and also, of
        course, a baz.'''))

print_string()
