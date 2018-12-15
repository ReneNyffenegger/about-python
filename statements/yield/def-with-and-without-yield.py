#!/usr/bin/python3


def FuncWithoutYield():
    return 42

def FuncWithYield():
    yield 42

print(type(FuncWithoutYield))
# <class 'function'>

print(type(FuncWithYield))
# <class 'function'>

retFuncWithoutYield = FuncWithoutYield()
retFuncWithYield    = FuncWithYield()

print(type(retFuncWithoutYield))
# <class 'int'>

print(type(retFuncWithYield))
# <class 'generator'>
