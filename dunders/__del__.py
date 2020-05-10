class CLS:

      def __init__(self, ident):
          self.ident = ident
          print('CLS.__init__() was called for ident = {}'.format(self.ident))

      def __del__(self):
          print('CLS.__del__() was called for ident = {}'.format(self.ident))

def F():

    print('entering F')
    obj_F = CLS('F')
    print('leaving F')


obj_ref_1= CLS('obj'  )
obj_ref_2=obj_ref_1

print('Calling F')
F()
print('returned from F')


print('calling del(obj_ref_1)')
del(obj_ref_1)
print('returned from del(obj_ref_1), calling del(obj_ref_2)')
del(obj_ref_2)
print('returned from del(obj_ref_2)')
