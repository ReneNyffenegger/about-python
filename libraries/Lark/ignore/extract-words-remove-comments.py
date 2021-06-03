import lark

parser = lark.Lark("""
start: word*

//
// Note the question mark before the word:
//   It allows to get the value of the word directly
//   with word.value when iterating over the
//   parsed text.
//   Without question mark, we'd be iterating over
//   Tree-objects rather than Token-objects.
//
?word: /\w+/

%import common.WS
%import common.CPP_COMMENT
%import common.C_COMMENT

%ignore WS
%ignore CPP_COMMENT
%ignore C_COMMENT
""")

parsed = parser.parse("""
one two // this is a comment and should not be extracted
three four /* another comment */ five
  six seven
""")

for word in parsed.children:
    print(word.value)
