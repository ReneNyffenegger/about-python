#!/usr/bin/python
import sqlite3
import os

if os.path.isfile('trx.db'):
   os.remove('trx.db')

db = sqlite3.connect('trx.db')

cur = db.cursor()

cur.execute('create table t (a number, b varchar)')

cur.execute("insert into t values (1, 'one')")
cur.execute("insert into t values (2, 'two')")

db.rollback()

cur.execute("insert into t values (3, 'three')")
cur.execute("insert into t values (4, 'four')")

db.commit()

for row in cur.execute('select * from t order by a'):  
    print("%2d: %s" % (row[0], row[1]))
