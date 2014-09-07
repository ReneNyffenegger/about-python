for i in range (-7, 7):
    try:
      print 1000/i
    except ZeroDivisionError:
      print "i is zero, division impossible" 
