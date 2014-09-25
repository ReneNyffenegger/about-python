# -*- coding: utf-8 -*-
import os
import sys
import sqlite3

db_filename = 'nested_loop.db'
if os.path.isfile(db_filename):
   os.remove(db_filename)

db = sqlite3.connect(db_filename)
db.text_factory = str

cur = db.cursor()

cur.execute('create table O (o int       )')
cur.execute('create table I (o int, i int)')

cur.execute('insert into O values (?   )' , ( 1 ,   ) )
cur.execute('insert into O values (?   )' , ( 2 ,   ) )
cur.execute('insert into O values (?   )' , ( 3 ,   ) )

cur.execute('insert into I values (?, ?)' , ( 1 , 11) )
cur.execute('insert into I values (?, ?)' , ( 1 , 12) )
cur.execute('insert into I values (?, ?)' , ( 1 , 13) )
cur.execute('insert into I values (?, ?)' , ( 1 , 14) )

cur.execute('insert into I values (?, ?)' , ( 2 , 21) )

cur.execute('insert into I values (?, ?)' , ( 3 , 31) )
cur.execute('insert into I values (?, ?)' , ( 3 , 32) )


def I(o):

    print "o: {:d}".format(o)
    for r in cur.execute('select i from I where o = ?', (o ,)):
        print "  i: {:d}".format(r[0])
       

def O():
    for r in cur.execute('select * from O'):
        I(r[0])

O()
