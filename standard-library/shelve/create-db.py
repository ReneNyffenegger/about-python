import shelve

db = shelve.open('test') # creates test.db

db['key-1'] = 'xyz'
db['key-2'] = [1, 2, 3]

db['key-1'] = {'num': 42}

#
# db[…] returns a copy, not a reference. Therefore
# the following statment does not change the content
# of the db:
#
db['key-1']['txt'] = 'Hello world'

db.close()
