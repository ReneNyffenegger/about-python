def Func():
    yield 'one'
    yield 'two'
    yield 'three'

for word in Func():
    print(word)
