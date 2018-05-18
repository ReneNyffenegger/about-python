#!/usr/bin/python
import json

#
#   Reading json data from a string
#
d = json.loads ('''

  {"foo":{"42":"forty-two",
           "8":"eight"},
    "bar":[{"key":"1"},
           {"key":"2"},
           {"key":"3"},
           {"key":"4"}]
   }
  
''')

print(d['foo']['42']) # forty-two

# -------------------------------
#
#  Reading json data from a file
#

json_file=open('file.json')
f=json.load(json_file)
print(f[2][1])            # Yes
print(f[3]['foo'])        # word
