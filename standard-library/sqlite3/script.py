import sqlite3
import os.path

if os.path.isfile('foo.db'):
   os.remove('foo.db')

db = sqlite3.connect('foo.db')

cur = db.cursor()

cur.execute('create table bar (a number, b varchar)')

cur.execute("insert into bar values (2, 'two')")

cur.execute('insert into bar values (?, ?)', (42, 'forty-two'))

cur.executemany('insert into bar values (?, ?)', [
  (4, 'four'),
  (5, 'five'),
  (7, 'seven'),
  (9, 'nine')
])

for row in cur.execute('select * from bar order by a'):  
    print "%2d: %s" % (row[0], row[1])
#  2: two
#  4: four
#  5: five
#  7: seven
#  9: nine
# 42: forty-two
