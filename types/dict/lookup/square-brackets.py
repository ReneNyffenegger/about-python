d = { 'num': 42, 'txt': 'Hello world' }

def printValOfKey(k):

    try:
       print(f'value for {k} is: {d[k]}')
    except KeyError:
       print(f'Key {k} does not exist')


printValOfKey('num'       )
printValOfKey('inexistent')
printValOfKey('txt'       )
