#
#    cursor.lastrowid returns the last inserted rowid
#
import os
import sys
import sqlite3

db_filename = 'cursor_lastrowid.db'
if os.path.isfile(db_filename):
   os.remove(db_filename)

def ins(a):
    cur.execute('insert into t(a) values (?)', (a, ))
    print('Inserted a record, lastrowid is ' + str(cur.lastrowid))

db = sqlite3.connect(db_filename)
cur = db.cursor()

cur.execute('create table t (id integer primary key, a)')

ins(42)
ins(99)
