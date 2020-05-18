
build_class_orig = __build_class__

def build_class_hook(func, className, *baseClasses, **kw):

    print('Class', className, 'is being created')
    print('  This class derives from the following base classes: {}'.format( ', '.join([cls.__name__ for cls in baseClasses]) ))

    return build_class_orig(func, className, *baseClasses, **kw)

import builtins
builtins.__build_class__ = build_class_hook

class BASE:

      def __init__(self, ident):
          self.ident = ident

      def printIdent(self):
          print(self.ident)


class DERIV(BASE):

      def __init__(self, ident):
          BASE.__init__(self, ident)


base  = BASE(1)
deriv = DERIV(2)

base.printIdent()
deriv.printIdent()
