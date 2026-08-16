#!/usr/bin/env python3

from skyfield.api import load

planets = load('de421.bsp')
earth, mars = planets['earth'], planets['mars']
ts = load.timescale()
t = ts.now()
ra, dec, distance = earth.at(t).observe(mars).radec()
print(ra, dec, distance)
