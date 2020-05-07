def F(p):
  #
  # p refers to the same object that was passed
  # when F was called:
  #
    print('id(p) = {}'.format(id(p)))

  # Create a new object and let p refer
  # to the new object. This has no effect
  # on the reference that was passed to F:
  #
    p=[11,22,33]

  #
  # Another id will be printed:
  #
    print('id(p) = {}'.format(id(p)))

# -------------------------------------

def G(q):
    print('id(q) = {}'.format(id(q)))
  #
  # No new object is created, thus
  # the caller will see the changed
  # values:
  #
    q[0] = 11
    q[1] = 22
    q[2] = 33

  #
  # Same id is printed as before:
  #
    print('id(q) = {}'.format(id(q)))

# -------------------------------------

V = [1, 2, 3]
print('id(V) = {}'.format(id(V)))

F(V)
for v in V:
    print(v) # prints 1, 2 and 3

G(V)
for v in V:
    print(v) # prints 11, 22, 33
