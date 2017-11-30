import time, random, requests

from xgoogle.search import GoogleSearch, SearchError

f = open('a.txt','wb')

for i in range(0,2):
    wt = random.uniform(2, 5)
    gs = GoogleSearch("about")
    gs.results_per_page = 1
    gs.page = i
    results = gs.get_results()
    time.sleep(wt)
    for res in results:
        f.write(res.url.encode("utf8"))
        f.write("\n")

print "Done"
f.close()


import urllib

def download_file(download_url):
response = requests.get(j)
with open('/Users/GrayFrost/Desktop/document.pdf', 'wb') as f:
    f.write(response.content)
    url = 'http://www.hrecos.org//images/Data/forweb/HRTVBSH.Metadata.pdf'

In [3]: response = requests.get(url)

with open('/tmp/metadata.pdf', 'wb') as f:
   ...:     f.write(response.text)