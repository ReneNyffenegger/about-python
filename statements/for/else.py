for i in range(1, 5):

    print('i = ' + str(i))

    for j in range(1, 3):


        print('  j = ' + str(j))
        if i == j:
           print('  i == j, breaking')
           break


    else:
        print('else reached, i = {}, j = {}'.format(i, j))
#
# i = 1
#   j = 1
#   i == j, breaking
# i = 2
#   j = 1
#   j = 2
#   i == j, breaking
# i = 3
#   j = 1
#   j = 2
# else reached, i = 3, j = 2
# i = 4
#   j = 1
#   j = 2
# else reached, i = 4, j = 2
