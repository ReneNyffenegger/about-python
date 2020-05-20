class Ex(Exception):

  def __init__(self, text):
      self.text = text

  def __str__(self):
      return self.text

class RES:

  def __enter__(self):
      print('__enter__')
      return self

  def __exit__(self, exType, exValue, traceBack):
      print(f'__exit__, exType: {str(exType)}, exValue: {str(exValue)}, traceBack: {str(traceBack)}')


try:

  print('')

  with RES():
       print('  A')

  print('')

  with RES():
       print('  B')
       raise Ex('Something bad')

except Ex as ex:
       print('')
       print(f'Caught exception {str(ex)}')
