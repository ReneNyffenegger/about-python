class A:
  def __init__(self, ident):
      print(f"  A's constructor, ident = {ident}")
      self.ident = ident

  def printIdent(self):
      print(self.ident)


class B(A):

  def __init__(self, ident):
  #   Call A's constructor:
      print("  B's constructor")
      A.__init__(self, ident)
        

class C(A):

  def __init__(self, ident):
  #   Note: A's constructor is not called
      print("  C's constructor")

print('Creating a B')
b = B(42)

print('Creating a C')
c = C(49)

b.printIdent()
# c.printIdent()
