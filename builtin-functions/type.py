print type( []               )         # <type 'list'>
print type( ['foo', 1 ]      )         # <type 'list'>
print type( {}               )         # <type 'dict'>
print type( ''               )         # <type 'str'>
print type( 1 == 0           )         # <type 'bool'>
print type( unicode('foo')   )         # <type 'unicode'>
print type( 'bar'            )         # <type 'str'>
print type(  0               )         # <type 'int'>
print type(  42              )         # <type 'int'>
print type(  42.42           )         # <type 'float'>
print type(  None            )         # <type 'NoneType'>
print type(lambda a: a       )         # <type 'function'>

class class_A(object):
      pass

print type(class_A           )         # <type 'type'>

instance_A=class_A()
print type(instance_A        )         # <class '__main__.class_A'>


print type(instance_A) is class_A      # True

class class_B(class_A):
      pass

instance_B=class_B();
print type(instance_B) is class_B      # True
print type(instance_B) is class_A      # False
print isinstance(instance_B, class_A)  # True
print isinstance(instance_B, class_B)  # True


# print type(  print         )                             # invalid
