class Base:
      def m(self):
          print('Base::m')

class Deriv(Base):
      def m(self):
          print('Deriv::m')

b = Base ()
d = Deriv()

b.m()
d.m()
