
# coding: utf-8

# In[1]:
# In[17]:

import os, pickle, re
dl = os.listdir('./outpdfs')


# In[16]:

dic = {}
count = 1
for doc in dl:
    if '.p' in doc:
        print (doc)
        dicb = {}
        dici = {}
        dicbi = {}
        f = open ('./outpdfs/' + doc, 'rb')
        r = pickle.load(f)
        for b in r[0][0]:
            dicb[b] = 'b'
        for i in r[0][1]:
            dici[i] = 'i'
        for bi in r[0][2]:
            dicbi[bi] = 'bi'
        x = re.sub('.p', '', doc)
        dic[x] = [dicb, dici, dicbi]
        print (count, x, 'completed', sep = ' ')
        count += 1
m = open ('../style.pckl', 'wb')
pickle.dump (dic, m)
m.close()

# In[ ]:



