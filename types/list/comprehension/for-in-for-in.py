numbers = [ [ 'one' , 'two' , 'three'],
            [ 'eins', 'zwei', 'drei' ],
            [ 'un'  , 'dos' , 'tres' ]
          ]

flat_list = [
        translation                       # <-- 3: evaluate translation, create list
             for language    in numbers   # <-- 1: iterate over each element in numbers, assign to language
             for translation in language  # <-- 2: iterate over each element in each language, assign to translation
      ]

print(flat_list)
#
#  ['one', 'two', 'three', 'eins', 'zwei', 'drei', 'un', 'dos', 'tres']
