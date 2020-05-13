def raise_if(condition):

    if condition:
       print('throwing execption because condition is true')
       raise Exception()

    else:
       print('condition is false, nothing thrown')


try:
     raise_if(True)
except:
     print('executed if exception was caught')
else:
     print('executed if no exception was caught')
finally:
     print('always executed')

print('-----------------')

try:
     raise_if(False)
except:
     print('executed if exception was caught')
else:
     print('executed if no exception was caught')
finally:
     print('always executed')
