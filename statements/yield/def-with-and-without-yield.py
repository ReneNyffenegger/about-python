#!/usr/bin/python3


def FuncWithoutYield():
    return 42

def FuncWithYield():
    yield 42

print(type(FuncWithoutYield))
print(type(FuncWithYield))
#
# <class 'function'>
# <class 'function'>

retFuncWithoutYield = FuncWithoutYield()
retFuncWithYield    = FuncWithYield()

print(type(retFuncWithoutYield))
print(type(retFuncWithYield))
#
# <class 'int'>
# <class 'generator'>
