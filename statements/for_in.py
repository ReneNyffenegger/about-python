d = {'foo':  42, 
     'bar': "forty-two",
     'baz': None}

print
for k in d:
    print "  ", k, " = ", d[k]

print
print "Using items()"
for k,v in d.items():
    print "  ", k, " = ", v
