d = { 'num': 42, 'txt': 'Hello world' }

def printValOfKey(k):
    print(f"value for {k} is: {d.get(k, '?')}")

printValOfKey('num'       )
printValOfKey('inexistent')
printValOfKey('txt'       )
