class A_CLASS:
      def whoAreYou(self):
          return 'a class'

class ANOTHER_CLASS:
      def whoAreYou(self):
          return 'another class'

class A_DERIVED_CLASS(A_CLASS):
      def whoAreYou(self):
          return 'A class that derives from ' + super().whoAreYou()

class ANOTHER_CLASS(ANOTHER_CLASS):
      def whoAreYou(self):
          return 'Another derived class that derives from ' + super().whoAreYou()

types =  (A_CLASS        ,
          ANOTHER_CLASS  ,
          A_DERIVED_CLASS,
          ANOTHER_CLASS)

objects = [ obj() for obj in types ]

for o in objects:
    for t in types:
        if isinstance(o, t):
           print(o.whoAreYou(), 'is an instance of', t.__name__)
        else:
           print(o.whoAreYou(), 'is not an instance of', t.__name__)
#
# a class is an instance of A_CLASS
# a class is not an instance of ANOTHER_CLASS
# a class is not an instance of A_DERIVED_CLASS
# a class is not an instance of ANOTHER_CLASS
# Another derived class that derives from another class is not an instance of A_CLASS
# Another derived class that derives from another class is an instance of ANOTHER_CLASS
# Another derived class that derives from another class is not an instance of A_DERIVED_CLASS
# Another derived class that derives from another class is an instance of ANOTHER_CLASS
# A class that derives from a class is an instance of A_CLASS
# A class that derives from a class is not an instance of ANOTHER_CLASS
# A class that derives from a class is an instance of A_DERIVED_CLASS
# A class that derives from a class is not an instance of ANOTHER_CLASS
# Another derived class that derives from another class is not an instance of A_CLASS
# Another derived class that derives from another class is an instance of ANOTHER_CLASS
# Another derived class that derives from another class is not an instance of A_DERIVED_CLASS
# Another derived class that derives from another class is an instance of ANOTHER_CLASS
#
