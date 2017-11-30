import pickle
import requests

r = open('../doi.pckl', 'rb')
m = pickle.load(r)

def download_file(download_url, name):
    response = requests.get(download_url)
    with open(name+".pdf", 'wb') as f:
        f.write(response.content)
        f.close()

x = []
for s in m:
    print (s[0])
    try:
        download_file("http://citeseerx.ist.psu.edu/viewdoc/download?doi="+s[2]+"&rep=rep1&type=pdf",s[1])
    except:
        x.append(s)
        continue
l = open('../dowfail.pckl', 'wb')
pickle.dump(x, l)