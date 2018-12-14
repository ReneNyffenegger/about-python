#!/usr/bin/python3

def globalFunc():
    print("globalFunc was called")
    return 'eggs'

print("next is definition of class TQ84")

class TQ84():

 # 
 #  The following two statements (print and calling globalFunc)
 #  are executed while this class definition is read by the
 #  parser (and not, as one might think) when the class
 #  is instantiaed.
 # 
    print("Within TQ84")
    x = globalFunc()

    def __init__(self, name):
     #
     #  However, these two statements are
     #  only executed when an instance of
     #  the class is created (but the def
     #  is executed)
     #
        print("TQ84.__init__ was called")
        self.name = name

 #
 #  Again, this print statement is executed
 #  during parsing of the class.
 #
    print("This line is after def __init__")

print("going to instantiate an instance")
foo = TQ84('foo')

print("going to instantiate another instance")
bar = TQ84('bar')
#
# next is definition of class TQ84
# Within TQ84
# globalFunc was called
# This line is after def __init__
# going to instantiate an instance
# TQ84.__init__ was called
# going to instantiate another instance
# TQ84.__init__ was called
