# -*- coding: utf-8 -*-
import os
import sys
import sqlite3

db_filename = 'non_ascii.db'
if os.path.isfile(db_filename):
   os.remove(db_filename)

db = sqlite3.connect(db_filename)
db.text_factory = str

cur = db.cursor()

cur.execute('create table T (a text)')

cur.execute('insert into T values (?)' , ( 'Tasse'     ,) )
cur.execute('insert into T values (?)' , ( 'Märchen'   ,) )
cur.execute('insert into T values (?)' , ( 'Butterbrot',) )
cur.execute('insert into T values (?)' , ( 'Säbel'     ,) )

# two records returned
print '\nselect * from T where a like "%ä%"'
for r in cur.execute('select * from T where a like "%ä%"'):
    print "  " + r[0]

# Note: no records returned. (At least not on Windows with Python 2.7)
print '\nselect * from T where upper(a) like "%Ä%"'
for r in cur.execute('select * from T where upper(a) like "%Ä%"'):
    print "  " + r[0]
