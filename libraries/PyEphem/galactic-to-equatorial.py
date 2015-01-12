#
# http://stackoverflow.com/questions/11169523/how-to-compute-alt-az-for-given-galactic-coordinate-glon-glat-with-pyephem
#

import ephem

def galacticToEquatorial(lon, lat):
    galactic   = ephem.Galactic(lon, lat)
    equatorial = ephem.Equatorial(galactic)

    print str(lon)+'/'+str(lat)+': RA='+str(equatorial.ra)+', dec='+str(equatorial.dec.real / 3.14156 * 180)


galacticToEquatorial(  '0:0:0',   '0:0:0')  # Galactic Center
galacticToEquatorial(  '0:0:0',  '90:0:0')  # Galactic North Pole
galacticToEquatorial(  '0:0:0', '180:0:0')  # Opposite Galactic Center
galacticToEquatorial(  '0:0:0', '270:0:0')  # Galactic South Pole
galacticToEquatorial( '90:0:0',   '0:0:0')  # Lat 90
galacticToEquatorial('270:0:0',   '0:0:0')  # Lat 270

