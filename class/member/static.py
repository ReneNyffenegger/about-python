class C:

 #
 # Define a class variable (aka static member):
 #
   creation_counter = 0

   def __init__(self):

     #
     # increment
     #
       C.creation_counter += 1

     #
     # Assign a value to self.created which
     # effectively creates an instance variable:
     #
       self.created = C.creation_counter

 #
 # Define a static method. Note the «@staticmethod»
 #
   @staticmethod
   def printCreationCounter():
       print('The current value of creation_counter is {}'.format(C.creation_counter))

 #
 # Define an instance-method:
 #
   def printCreated(self):
       print('This instance has creation number {}'.format(self.created))


C.printCreationCounter()
#
#  The current value of creation_counter is 0


obj_1 = C()
obj_2 = C()

C.printCreationCounter()
#
# The current value of creation_counter is 2

obj_3 = C()


obj_3.printCreated()
#
# This instance has creation number 3

obj_1.printCreated()
#
# This instance has creation number 1

obj_2.printCreated()
#
# This instance has creation number 2
