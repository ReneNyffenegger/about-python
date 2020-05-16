seq = [
  ( 'Key'        , 'Value'         ),
  [ 'Another key', 'Another Value' ]
]

d = dict(seq)

for k, v in d.items():
    print(k, ':', v)
#
#  Key : Value
#  Another key : Another Value
