def printTypeOfType(obj):

    type_of_obj  = type(obj        )
    type_of_type = type(type_of_obj)

    print(f'obj          = {obj         }')
    print(f'type_of_obj  = {type_of_obj }')
    print(f'type_of_type = {type_of_type}')
    print('')

printTypeOfType( 42          )
#
# obj          = 42
# type_of_obj  = <class 'int'>
# type_of_type = <class 'type'>

printTypeOfType( 99.9        )
#
# obj          = 99.9
# type_of_obj  = <class 'float'>
# type_of_type = <class 'type'>

printTypeOfType('Hello world')
#
# obj          = Hello world
# type_of_obj  = <class 'str'>
# type_of_type = <class 'type'>

printTypeOfType(printTypeOfType)
#
# obj          = <function printTypeOfType at 0x000001F329B07F70>
# type_of_obj  = <class 'function'>
# type_of_type = <class 'type'>
