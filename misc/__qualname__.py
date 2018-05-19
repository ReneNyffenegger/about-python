#!/usr/bin/python

class ABC:
    def __init__(self):
        pass

    class DEF:
        def meth():
            pass


print(ABC         .__qualname__)
print(ABC.DEF     .__qualname__)
print(ABC.DEF.meth.__qualname__)
