import json

d = json.loads ('''

  {"foo":{"42":"forty-two",
           "8":"eight"},
    "bar":[{"key":"1"},
           {"key":"2"},
           {"key":"3"},
           {"key":"4"}]
   }
  
''')

print d['foo']['42'] # forty-two
