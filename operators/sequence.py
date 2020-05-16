print ( [ 42, 'Hello world'    ]  <  [ 42, 'ZZZZ'            ] )  # True
print ( [ 42, 'Hello world'    ]  <  [ 42, 'Hello world', 1  ] )  # True
print ( [ 42, 'Hello world', 1 ]  <  [ 42, 'Hello world'     ] )  # False
print ( [  7, (3,2,1)      , 8 ]  <  [  7, (9, 8, 7)    , 1  ] )  # True
