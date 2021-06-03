import lark

grammar_without_question_mark = """
start:   rul   rul

rul:       /\w+/  /\w+/
   |  "("  /\w+/  ")"

%ignore " "
"""

# ---------------------


grammar_with_question_mark = """
start:   rul   rul

?rul:      /\w+/  /\w+/
   |  "("  /\w+/  ")"

%ignore " "
"""

# ---------------------

def parse(grammar):

    parser = lark.Lark(grammar)
    parsed = parser.parse('foo bar (baz)')

    for ch_1 in parsed.children:

        if   isinstance(ch_1, lark.Tree):
             print('Tree with name ' + str(ch_1.data))

             for ch_2 in ch_1.children:
                 print('   ' + ch_2.value)

        elif isinstance(ch_1, lark.Token):
             print('Token with value ' + str(ch_1.value))


parse(grammar_without_question_mark)

print('-' * 30)

parse(grammar_with_question_mark   )
