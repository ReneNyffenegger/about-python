#
#   http://stackoverflow.com/a/531376/180275
#
funcs = []

for x in range(5):
    funcs.append(lambda: x)

print [f() for f in funcs]     #  [4, 4, 4, 4, 4]

# ---

funcs = []
for x in range(5):
  funcs.append(lambda x=x: x)
  
print [f() for f in funcs]    #  [0, 1, 2, 3, 4]
