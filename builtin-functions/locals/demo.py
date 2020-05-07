def F():

    if 'x' in locals():
       print('locals() contains x')
    else:
       print('locals() does not contain x')

    x = 42

    if 'x' in locals():
       print('locals() contains x')
    else:
       print('locals() does not contain x')

F()
