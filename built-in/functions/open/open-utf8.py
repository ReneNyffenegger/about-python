with open('file.utf8', 'r', encoding='utf-8') as fil:
     for lin in fil:
         lin=lin.rstrip('\n\r')
         print(lin)
