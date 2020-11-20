import argparse

argParser = argparse.ArgumentParser()

argParser.add_argument('-flag'   , action = 'store_true', help = 'Specify a true/false option'                          )
argParser.add_argument('-number' , type   =  int        , help = 'What is the number'                                   )
argParser.add_argument('-text'   , type   =  str        , help = 'What is the text'           , default  = 'Hello world')
argParser.add_argument('-req'    , type   =  int        , help = 'A required argument'        , required =  True        )

parsedArgs = argParser.parse_args()

if parsedArgs.flag:
   print('You specified the flag')
else:
   print('You did not specify the flag')

print('The number is ' + str(parsedArgs.number))
print('The text   is ' +     parsedArgs.text   )
print('req        is ' + str(parsedArgs.req   ))
