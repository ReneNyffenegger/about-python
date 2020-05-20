from contextlib import contextmanager

@contextmanager
def aResource():

    print('Acquiring a resource')
    try:
       yield

    finally:
       print('releasing the resource')

with aResource():
     print('  do something while the resource is acquired')
