# http://stackoverflow.com/questions/16694907/how-to-download-large-file-in-python-with-requests-py

import requests

f = open ('README.md.downloaded', 'wb')
r = requests.get('https://raw.githubusercontent.com/ReneNyffenegger/about-python/master/libraries/requests/README.md', stream = True)

for chunk in r.iter_content(chunk_size = 1024):
    if chunk: # filter out keep-alive new chunks
       f.write(chunk)
       f.flush()

f.close()
