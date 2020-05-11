import urllib.request

url = 'https://raw.githubusercontent.com/ReneNyffenegger/about-python/master/standard-library/urllib/request/demo.py'

html_text = urllib.request.urlopen(url).read()
#
# The type of html_text is 'bytes'
#

print(html_text.decode('utf-8'))

urllib.request.urlretrieve (url, 'downloaded-script.py');
