from lark import Lark

#
#   Initialize parser with «EBNF» of the language
#
parser = Lark("""
start: item+

item: DIGIT  -> dig
    | CHAR   -> chr

CHAR : ("a" .. "z")
DIGIT: ("0" .. "9")
""")

#
#   Parse program. Note that langauge does not allow
#   for white spaces:
#
parsed = parser.parse('abc123xy9')

for i in parsed.children:
    rule     = i.data
    print('Rule {} was found, 1st child is {}'.format(rule, i.children[0]))
