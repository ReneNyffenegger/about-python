import re

reNumbers = re.compile('(\d+)')

def getNumber(txt):

   if m := reNumbers.search(txt):
      print('The extracted number is ' + m.group(1))

   else:
      print('No number found in ' + txt)


getNumber('hello world')
getNumber('the number is 42, what else?')
