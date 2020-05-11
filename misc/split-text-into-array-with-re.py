import re

txt = """\
Foo, bar and baz. Those three words! Do
new lines work, too? Yes: they do.\
"""

words=re.split('[ .,?;:!\n]+', txt)

for word in words:
    print(word)
