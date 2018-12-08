#!/usr/bin/python3

#
#     Defining a base …
#
class Base:
      pass

#
#     … and  a derived class:
#
class Deriv(Base):
      pass


#     ----------------------------------------
#
#     Using isinstance(…)
#
if    isinstance(Base(), Base):
      print('Base is instance of Base')
else:
      print('Base is not instance of Base')

if    isinstance(Deriv(), Base):
      print('Deriv is instance of Base')
else:
      print('Deriv is not instance of Base')

#     ----------------------------------------
#
#     Using type(…)
#
if    type(Base()) == Base:
      print('Base is type Base')
else:
      print('Base is not type Base')

if    type(Deriv()) == Base:
      print('Deriv is type Base')
else:
      print('Deriv is not type Base')

# Base is instance of Base
# Deriv is instance of Base
# Base is type Base
# Deriv is not type Base
