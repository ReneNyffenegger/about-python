import os

def readALine(fil):
    try:
       lin = next(fil)
       print('Line that was read is:', lin.rstrip("\n"))
       return True
    except StopIteration:
       return False


fil = open(os.path.dirname(__file__) + '/lines.txt', 'r')

while readALine(fil): pass

