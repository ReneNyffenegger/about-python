#
#      Python 3:  
#        import urllib.request
#        urllib.request.urlopen(...)
#
import urllib

html_text = urllib.urlopen('https://raw.githubusercontent.com/ReneNyffenegger/about-python/master/standard-library/urllib/script.py').read()
print html_text

# --

urllib.urlretrieve ('https://raw.githubusercontent.com/ReneNyffenegger/about-python/master/standard-library/urllib/script.py', 'downloaded-script.py');
