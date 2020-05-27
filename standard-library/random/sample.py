import random

#
#  Choose two (distinct) random fruits, in random order:
#
for fruit in random.sample( ['apple', 'pear', 'orange', 'cherry', 'banana'], 2):
    print(fruit)
