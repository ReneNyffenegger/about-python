#
#     Check if a function is callable
#

func_ref = sorted

if    callable(func_ref):
      print('func_ref is callable'    )
else:
      print('func_ref is not callable')

#
#  func_ref is callable
#

#     ------------------------

#
#     Define a class without a __call__() method:
#
class CLS:
      pass

#     ------------------------

#
#     Create an instance of this class
#

obj_ref = CLS()

if    callable(obj_ref):
      print('obj_ref is callable'    )
else:
      print('obj_ref is not callable')
#
#  obj_ref is not callable
#


#     ------------------------

#
#     Add a __call__ attribute to the
#     CLS class:
#

setattr(CLS, '__call__', 'foo')

if    callable(obj_ref):
      print('obj_ref is callable'    )
else:
      print('obj_ref is not callable')

#
#     Of course, the string 'foo' is not
#     callable. Therefore, the following
#     call would produce an error message
#     if exuected
#
#     obj_ref()
#

#
#     Therefore, add a «real» function reference
#     so that the class is not only callable
#     but also can be called:
#
setattr(CLS, '__call__', lambda self, n: n ** 2)


print(obj_ref(7))
#
#  49
#
