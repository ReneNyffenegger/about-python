class CLS:

  def __init__(self, ident):
      self.ident = ident
      print(f'__init__, ident = {self.ident}')

  def identify(self):
      print(f'I am {self.ident}')
      
  def __enter__(self):
      print(f'{self.ident}: __enter__')
      return CLS('created in __enter__')

  def __exit__(self, type, value, traceback):
      print(f'{self.ident}: __exit__')


print('Going to use with statement:')
with CLS('xyz') as obj:
     obj.identify()

print('Finished with with statement')
