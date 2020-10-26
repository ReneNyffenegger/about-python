from lark import Lark

parser = Lark("""
start: item+

item: DIGIT -> dig
    | CHAR  -> chr

CHAR : ("a" .. "z")
DIGIT: ("0" .. "9")

%import common.WS
%ignore WS
""")

parsed = parser.parse("""
  ab c1
  23x y 9
""")

for i in parsed.children:
    rule     = i.data
    print('Rule {} was found, 1st child is {}'.format(rule, i.children[0]))
