import sqlite3
import os.path

if os.path.isfile('db'):
   os.remove('db')

db = sqlite3.connect('db')
cur = db.cursor()

cur.execute('begin transaction')
cur.execute('create table T (id integer primary key, txt text unique)')

cur.executemany('insert into T values(?, ?)', [
   (42, 'forty-two'  ),
   (99, 'ninety-nine'),
   ( 0, 'zero'       ),
   ( 7, 'seven'      ),
   (-1,  None        ), # Note null (None) can be inserted multiple times
   (-2,  None        ), # inspite of the unique constraint
])

cur.execute('commit')

def select_id(txt):
    if txt != None:
       res = cur.execute('select id from T where txt = ?', (txt, ))
    else:
       res = cur.execute('select id from T where txt is null')

    row = res.fetchone()

    if row:
       print('ID of ' + str(txt) + ' is ' + str(row[0]))
    else:
       print('No row found for ' + str(txt))

select_id('ninety-nine')
select_id('forty-two'  )
select_id( None        )
select_id('inexisting' )
