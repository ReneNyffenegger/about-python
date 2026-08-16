#!/usr/bin/env python3

from skyfield.api import load

planets = load('de421.bsp')
earth   = planets['earth' ]
mars    = planets['mars'  ]

t_now  = load.timescale().now()

ra, dec, distance = earth.at(t_now).observe(mars).radec()

print(ra, dec, distance)
