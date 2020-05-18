class BASE():

      def __init__(self, ident):
          print(f'An instance of BASE is being initialized, ident = {ident}')
          self.ident = ident

      def __init_subclass__(cls, *a, **kw):
          print('A subclass of BASE is being created')

print('Going to create DERIV:')

class DERIV(BASE):

      def __init__(self, ident):
          print(f'An instance of DERIV is being initialized, ident={ident}')
          BASE.__init__(self, ident)

print('Finished with creation of DERIV')

base_1  = BASE(1)
deriv_2 = DERIV(2)
deriv_3 = DERIV(3)
