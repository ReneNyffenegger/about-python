#
#      Python 3:  
#        import urllib.request
#        urllib.request.urlopen(...)
#
import urllib

html_text = urllib.urlopen('https://github.com/ReneNyffenegger/about-python/tree/master/standard-library/urllib').read()
print html_text
