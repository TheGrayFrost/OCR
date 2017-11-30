import pickle
import requests
from bs4 import BeautifulSoup
import re

r = open('paperlist.pckl', 'rb')
m = pickle.load(r)

def finddoi(query):
    query=query.lower()
    query=query.replace(" ","+")
    tt="http://citeseerx.ist.psu.edu/search?q="+query+"&submit.x=8&submit.y=16&submit=Search&sort=rlv&t=doc"
    rr = requests.get(tt, auth=('user', 'pass'))
    soup=BeautifulSoup(rr.text,'html.parser')
    k=soup.find('a', class_="remove doc_details")
    j=k.get_text()
    j=j.lower()
    j=j.strip()
    x=re.search('doi=(.*?)&', k['href'])
    found="no"
    if m:
        found = x.group(1)
    return(j,found) 

doi=dict()
l = []
i=1
for kk in m:
    print(i)
    i+=1
    try:
        a,b=finddoi(kk[1])
        doi.update({a:b})
    except:
        l.append(kk)
        continue

with open("doi.pckl","wb") as xx:
    pickle.dump (doi, xx)
with open("fail.pckl","wb") as yy:
    pickle.dump (l, yy)
