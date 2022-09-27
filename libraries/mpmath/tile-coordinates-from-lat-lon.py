import sys
import mpmath as mp

if len(sys.argv) != 4:
   print('expected lat lon zoom')
   quit()

lat_deg = float(sys.argv[1])
lon_deg = float(sys.argv[2])
zoom    = int  (sys.argv[3])
   
lat_rad = mp.radians(lat_deg)
n = 2 ** zoom

x = n * ((lon_deg + 180) / 360)
y = n * (1 - (mp.log(mp.tan(lat_rad) + mp.sec(lat_rad)) / mp.pi)) / 2

print('x = %d, y = %d' % (x, y))
