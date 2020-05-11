import re

text = """\
This is the first line.
The second one.
The final one."""

re_1st_line = re.compile('.*')

first_line = re.match(re_1st_line, text)

print(first_line[0])
