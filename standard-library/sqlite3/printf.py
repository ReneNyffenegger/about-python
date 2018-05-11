#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import sqlite3

db_filename = 'printf.db'
if os.path.isfile(db_filename):
   os.remove(db_filename)

db = sqlite3.connect(db_filename)
db.text_factory = str

cur = db.cursor()

# printf only added with sqlite version 3.8.3, compare http://stackoverflow.com/questions/26149879/why-cant-i-use-printf-with-sqlite-when-executed-in-python
cur.execute(r'create table foo as select printf("%5.2f", 42.424242) bar')
