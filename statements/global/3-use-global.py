num = 42

def printNumAndIncrement(i):
    global num
    print(num)
    num = num + i

printNumAndIncrement(57)
printNumAndIncrement( 1)
