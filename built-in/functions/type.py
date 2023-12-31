#!/usr/bin/python3

print ( type( []                    ))         # <class 'list'>
print ( type( ['foo', 1 ]           ))         # <class 'list'>
print ( type( {}                    ))         # <class 'dict'>
print ( type( ''                    ))         # <class 'str'>
print ( type( 1 == 0                ))         # <class 'bool'>
print ( type( True                  ))         # <class 'bool'>
print ( type( str  ('foo')          ))         # <class 'str'>
print ( type( bytes('foo', 'utf-8') ))         # <class 'bytes'>
print ( type( 'bar'                 ))         # <class 'str'>
print ( type(  0                    ))         # <class 'int'>
print ( type(  42                   ))         # <class 'int'>
print ( type(  42.42                ))         # <class 'float'>
print ( type(  None                 ))         # <class 'NoneType'>
print ( type( lambda a: a           ))         # <class 'function'>
print ( type( type( 0 )             ))         # <class 'type'>
print ( type( list                  ))         # <class 'type'>
print ( type( dict                  ))         # <class 'type'>
print ( type( type.__dict__         ))         # <class 'mappingproxy'>

print ("---")

def   f(): pass
print ( type( f.__code__            ))         # <class 'code'>


class class_A(object): pass
print ( type(class_A          ))         # <type 'type'>

instance_A=class_A()
print ( type(instance_A       ))         # <class '__main__.class_A'>

print ( type(instance_A) is class_A )    # True

class class_B(class_A): pass

instance_B=class_B();
print ( type(instance_B) is class_B    )  # True
print ( type(instance_B) is class_A    )  # False
print ( isinstance(instance_B, class_A))  # True
print ( isinstance(instance_B, class_B))  # True

print ( type(  print                  ))  # <class 'builtin_function_or_method'>

import sys
print ( type( sys.implementation      ))  # <class 'types.SimpleNamespace'>
