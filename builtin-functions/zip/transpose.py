numbers = [ ( 'one' , 'two' , 'three'),
            ( 'eins', 'zwei', 'drei' ),
            ( 'un'  , 'dos' , 'tres' )
          ]

transposed = list(zip(*numbers))

print(transposed)
