from   bs4 import BeautifulSoup
import requests

html_text=requests.get('https://github.com/ReneNyffenegger/about-python/tree/master/libraries/BeautifulSoup/script.py').text

soup = BeautifulSoup(html_text)

print "Title:          ", soup.title
print "  .name:        ", soup.title.name
print "  .string       ", soup.title.string
print "  .parent.name: ", soup.title.parent.name

print

print "Links:"

for a in soup.find_all('a'):
    print "  %-30s: %s" % (a.string, a.get('href'))
