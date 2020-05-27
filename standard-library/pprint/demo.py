import pprint

data = {
    "foo":{ "42":"forty-two", "8" :"eight" }, "bar":[
    {"key":"1", "value": "one"  }, {"key":"2", "value":
    "two"  }, {"key":"3", "value": "three"}, {"key":"4",
    "value": "four" } ] }

pprint.pprint(data)

#
#  {'bar': [{'key': '1', 'value': 'one'},
#           {'key': '2', 'value': 'two'},
#           {'key': '3', 'value': 'three'},
#           {'key': '4', 'value': 'four'}],
#   'foo': {'42': 'forty-two', '8': 'eight'}}
