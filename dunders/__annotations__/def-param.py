def F(num: 'A number',
      txt: 'A text'   ='Hello World'):

    print('num:', num)
    print('txt:', txt)
    print('')

F(42)
F(txt = 'good bye', num = 99)

print('Annotations:')
for annot, val in F.__annotations__.items():
    print('{:4s}: {}'.format(annot, val))
