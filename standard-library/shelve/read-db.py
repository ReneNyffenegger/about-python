import shelve

db = shelve.open('test')

for key in db.keys():
    print(key + ': ' + str(db[key]))
