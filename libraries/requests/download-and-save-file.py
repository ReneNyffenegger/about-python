import requests

f = open ('script.downloaded', 'wb')
r = requests.get('https://raw.githubusercontent.com/ReneNyffenegger/about-python/master/libraries/requests/download-and-save-file.py', stream = True)

for chunk in r.iter_content(chunk_size = 1024):
    if chunk: # filter out keep-alive new chunks
       f.write(chunk)
       f.flush()

f.close()
