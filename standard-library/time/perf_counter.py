#!/usr/bin/python3

import time

def doSomething():
    ret = 0
    for i in range(0, 100):
        ret += i**i

    return ret

t0 = time.perf_counter()
print(doSomething())
t1 = time.perf_counter()

tExec = t1 - t0

print(f"Execution of doSomething took {tExec:.7f} seconds.")
