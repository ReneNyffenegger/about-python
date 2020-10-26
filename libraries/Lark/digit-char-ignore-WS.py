from lark import Lark
from lark import lexer

parser = Lark("""
start: whitespace item+

item: DIGIT whitespace -> dig
    | CHAR  whitespace -> chr

whitespace: WS*

CHAR : ("a" .. "z")
DIGIT: ("0" .. "9")

WS: (" " | "\\n" | "\\t")
""")

parsed = parser.parse("""
  ab c1
  23x y 9
""")

for i in parsed.children:
    rule     = i.data
    if rule in ['dig', 'chr']:
       print('Rule {} was found, 1st child is {}'.format(rule, i.children[0]))
