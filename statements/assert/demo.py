lst = []

try:
   assert len(lst)

   print('-'.join(lst))

except AssertionError:
   print('assertion failed')
