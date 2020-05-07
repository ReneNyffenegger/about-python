num = 42

def printNumAndIncrement(i):
  #
  # The following print statement throws
  #
  #   UnboundLocalError: local variable 'num' referenced before assignment
  #
    print(num)
  
    num = num + i

printNumAndIncrement(57)
