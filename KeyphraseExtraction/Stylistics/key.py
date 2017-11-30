import re, pickle, os

pwd = os.getcwd()
dirlist = os.listdir(pwd)

h = open("../keywords.pckl", "wb")

keyphrase = {}

# collecting the keywords
for b in range(0, len(dirlist)):
    if ".key" in dirlist[b]:
		f = open (pwd + '/' + dirlist[b])
		acmkey = dirlist[b].replace('.key', '')
		g = f.read()
		g = re.sub("[^a-zA-Z]", " ", g)
		g = g.lower()
		keyword = g.split()
		for w in keyword:
			keyphrase[w] = 1

pickle.dump (keyphrase, h)

h.close()

