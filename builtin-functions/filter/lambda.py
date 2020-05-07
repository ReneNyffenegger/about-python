#!/usr/bin/python

nums  = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

#
#  Use a lambda function to filter the numbers whose length
#  is less or equal to four characters:
#
nums_ = filter(lambda L: len(L) <= 4, nums)

for num in nums_:
    print(num)
