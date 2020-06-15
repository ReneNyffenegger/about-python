list_en = [ 'one' , 'two' , 'three', 'four'   ]
list_es = [ 'un'  , 'dos' , 'tres' , 'cuatro' ]
list_de = [ 'eins', 'zwei', 'drei' , 'vier'   ]

for word_en, word_es, word_de in zip(list_en, list_es, list_de):
    print(f' {word_en:5}  {word_es:6}  {word_de}')
#
#   one    un      eins
#   two    dos     zwei
#   three  tres    drei
#   four   cuatro  vier
