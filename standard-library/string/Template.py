import string

templ = string.Template('One ${thing} costs ${price}')

for item in ( {'thing': 'apple', 'price':     0.65 },
              {'thing': 'car'  , 'price': 24999    },
              {'thing': 'tea'  , 'price':     2.18 }):

    print(templ.substitute(**item))
#
#  One apple costs 0.65
#  One car costs 24999
#  One tea costs 2.18
