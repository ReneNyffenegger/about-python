d = {}

d['one'         ] =  1
d['two'         ] =  2
d['three'       ] =  3
d['four'        ] =  4
d['ninety-nine' ] = 99


del d['three']

try:
   del d['XXXX']
except KeyError as e:
   print('Expected KeyError: {:s}'.format(str(e)))

for k, v in d.items():
   print('{:s} = {:d}'.format(k, v))
