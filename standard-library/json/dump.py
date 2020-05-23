import json

obj = {
   'num':  42,
   'txt': 'Hello world',
   'lst': [ 1, 2, 3 ],
   'dct': { 'k1': 'one', 'k2': 'two'}
}

print(json.dumps(obj))
#
#  {"num": 42, "txt": "Hello world", "lst": [1, 2, 3], "dct": {"k1": "one", "k2": "two"}}

with open('dumped.json', 'w') as df:
    json.dump(obj, df)
