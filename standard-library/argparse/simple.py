import argparse

argParser = argparse.ArgumentParser()

argParser.add_argument('-flag'   , action = 'store_true', help = 'Specify a true/false option')
argParser.add_argument('-number' , type   =  int        , help = 'What is the number')

parsedArgs = argParser.parse_args()

if parsedArgs.flag:
   print('You specified the flag')
else:
   print('You did not specify the flag')

print('The number is ' + str(parsedArgs.number))
