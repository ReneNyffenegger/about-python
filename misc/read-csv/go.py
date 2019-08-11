#!/usr/bin/python3

csv = open('data.csv')

#
#  Skip header
#
next(csv)

print(' col_1 | col_2 | col_3')
print(' ------+-------+------')
for line in csv:

    line = line.rstrip()

    values=line.split(',')

    val_1 = values[0]
    val_2 = values[1]
    val_3 = values[2]

    if val_1 == '':
       val_1 =  '-'
    if val_2 == '':
       val_2 =  '-'
    if val_3 == '':
       val_3 =  '-'

    print(' {:<5} | {:<5} | {:<5}'.format(val_1, val_2, val_3))

