import os
import sqlite3

db_filename = 'returning-rowid.db'
if os.path.isfile(db_filename):
   os.remove(db_filename)

db = sqlite3.connect(db_filename)

cur = db.cursor()

cur.execute('create table T (a text, b integer)')

print(cur.execute('insert into T values (?, ?) returning rowid' , ('abc', 99)).fetchone()[0])
