import requests


gotten = requests.get('https://raw.githubusercontent.com/ReneNyffenegger/about-python/master/libraries/requests/get.py')

print 'Status code: ', gotten.status_code
print "Headers:";

for header in gotten.headers:
    print "  %-30s: %s" % (header, gotten.headers[header])

print 'Encoding: ', gotten.encoding

print

print gotten.text
