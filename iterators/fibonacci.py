#!/usr/bin/python3

class Fibonacci():
    def __init__(self, howMany):
        self.counter = howMany
        self.curFib = 0
        self.nextFib = 1

    def __iter__(self):
     #
     #  Return an object that exposes an __next__ method.
     #  self (whose type is Fibonacci) is such an object:
     #
        return self

    def __next__(self):

        if self.counter == 0:
        #
        #  We have returned the count of fibonacci numbers
        #  asked for… stop the iteration:
        #
           raise StopIteration

        self.counter -= 1

        nextFib       = self.curFib + self.nextFib
        self.curFib   = self.nextFib
        self.nextFib  = nextFib

        return self.curFib


fib_10 = Fibonacci(10)

for fib in fib_10:
    print(fib)
