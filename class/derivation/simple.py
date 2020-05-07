class Base:
      def m(self):
          print('Base::m')

class Deriv(Base):
      pass

d = Deriv()
d.m()
