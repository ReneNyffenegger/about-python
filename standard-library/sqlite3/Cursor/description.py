import sqlite3

db  = sqlite3.connect(':memory:')
cur = db.cursor()

db.execute("create table t (c1, c2, c3)")
db.execute("insert into t values('foo', 1, 'one'  )")
db.execute("insert into t values('bar', 2, 'two'  )")
db.execute("insert into t values('baz', 3, 'three')")

colWidth = 6

first = True
for rec in cur.execute('select * from t'):
    if first:
       for colName in [colDesc[0] for colDesc in cur.description]:
           print(' ', end='')
           print(colName.ljust(colWidth, ' '), end='')

       print('')

       for colNo in range(len(cur.description)):
           print(' ', end='')
           print('-'.ljust(colWidth, '-'), end='')

       print('')

       first = False

    for colNo in range(len(cur.description)):
        print(' ', end='')
        print(str(rec[colNo]).ljust(colWidth, ' '), end='')

    print('')
