#!/usr/bin/python3

def globalFunc():
    print("globalFunc was called")
    return 'eggs'

print("next is definition of class TQ84")

class TQ84():

    print("Within TQ84")
    x = globalFunc()

    def __init__(self, name):
        print("TQ84.__init__ was called")
        self.name = name

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
