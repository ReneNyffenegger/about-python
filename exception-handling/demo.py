class  Ex_Base(BaseException):
       pass

class  Ex_Deriv(Ex_Base):
       pass

#      --------------------------------------

try:
       print('Before raising the exception')
       raise Ex_Deriv()
       print('After raising the exception')

except Ex_Deriv as e:               # Order of except statements is important.
       print('Ex_Deriv caught')     # Try to catch the more concrete class first.

except Ex_Base as e:
       print('Ex_Base caught')


#      --------------------------------------

try:
       print('Before raising the exception')
       raise Ex_Deriv()
       print('After raising the exception')

except Ex_Base as e:                # Probably wrong order.
       print('Ex_Base caught')

except Ex_Deriv as e:
       print('Ex_Deriv caught')
