#!/usr/bin/python
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

def generateData():
    for i in range(4):
        yield i, '*' * i
#
#  0:
#  1: *
#  2: two
#  2: **
#  3: ***
#  4: four
#  5: five
#  7: seven
#  9: nine
# 42: forty-two


cur.executemany('insert into bar values (?, ?)', generateData())

for row in cur.execute('select * from bar order by a'):
    print("{:2d}: {:s}".format(row[0], row[1]))

print('---')
# for row in cur.execute('select b from bar where a = ?',   42    ):     # ValueError: parameters are of unsupported type
# for row in cur.execute('select b from bar where a = ?', ( 42  ) ):     # ValueError: parameters are of unsupported type
# for row in cur.execute('select b from bar where a = ?',  '42'   ):     # sqlite3.ProgrammingError: Incorrect number of bindings supplied. The current statement uses 1, and there are 2 supplied.
# for row in cur.execute('select b from bar where a = ?', ('42' ) ):     # sqlite3.ProgrammingError: Incorrect number of bindings supplied. The current statement uses 1, and there are 2 supplied.
for   row in cur.execute('select b from bar where a = ?', ('42',) ):
    print(row[0])
    # forty-two
