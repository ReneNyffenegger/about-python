builtin_types = {}

def ensureTypeInDict(t):
    global builtin_types

    if not id(t) in builtin_types:

       builtin_types[id(t)] = {
           'name'    :  t.__name__,
           'aliases' : [],          # special key to store names of aliases (for example: OSError is EnvironmentError is IOError is WindowsError)
           'children': []           # type ids of children
       }

for builtin_name in dir(__builtins__) + ['builtin_function_or_method', 'module']:

    if   builtin_name == 'builtin_function_or_method':
         builtin_obj = type(dir)

    elif builtin_name == 'module':
         builtin_obj = __builtins__.__class__
    else:
         builtin_obj = getattr(__builtins__, builtin_name)

    builtin_type = builtin_obj

    if not issubclass(type(builtin_type), type):
       continue

    if builtin_type is object:
       continue

    assert len(builtin_type.__bases__) == 1

    type_name = builtin_type.__name__
    base_name = builtin_type.__bases__[0].__name__
    base_type = getattr(__builtins__, base_name)

    ensureTypeInDict(builtin_type)
    ensureTypeInDict(base_type   )

    if not id(builtin_type) in builtin_types[id(base_type)]['children']:
       builtin_types[id(base_type)]['children'].append(id(builtin_type))

    if builtin_name != type_name:
       builtin_types[id(builtin_type)]['aliases'].append(builtin_name)


def printTypeChildren(typeId, indent = -1):

    if indent >= 0:
       print('  ' * indent, end='')
       print(builtin_types[typeId]['name'], end='')

       if builtin_types[typeId]['aliases']:
          print(' ('                                       +
               ', '.join(builtin_types[typeId]['aliases']) +
               ')',
               end='')

       print('')

    for child_id in sorted(builtin_types[typeId]['children'], key=lambda λ: builtin_types[λ]['name'].upper()):
        printTypeChildren(child_id, indent+1)


printTypeChildren(id(object))
