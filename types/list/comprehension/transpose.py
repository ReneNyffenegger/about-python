numbers = [ [ 'one' , 'two' , 'three'],
            [ 'eins', 'zwei', 'drei' ],
            [ 'un'  , 'dos' , 'tres' ]
          ]

transposed = [
    [ translation[number] for translation in numbers            ]
                          for number      in range(len(numbers))
]

print(transposed)
#
#  [['one', 'eins', 'un'], ['two', 'zwei', 'dos'], ['three', 'drei', 'tres']]
