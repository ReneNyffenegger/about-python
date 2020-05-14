def F(par_1, par_2, par_3, par_4, par_5):

    print('par_1:', par_1)
    print('par_2:', par_2)
    print('par_3:', par_3)
    print('par_4:', par_4)
    print('par_5:', par_5)
    print('')


tup = 'T1', 'T2'
dct = {'par_4': 'D4',
       'par_5': 'D5',
       'par_3': 'D3'}

lst = [ 'L3', 'L4', 'L5' ]

F(*tup, **dct)
F(*tup,  *lst)
