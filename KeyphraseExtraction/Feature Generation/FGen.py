import re, os, pickle
from nltk import word_tokenize, pos_tag
from nltk.corpus import stopwords
import csv

pwd = os.getcwd()
dirlist = os.listdir(pwd)

# In[109]:

g = open("../keywords.pckl", "rb")
keyphrase = pickle.load(g)
g.close()

# In[110]:

ff = open("../featuresless0.csv", "w")
writer = csv.writer(ff)
count = 1

docs = {}

for b in range(0, len(dirlist)):
	if ".txt" in dirlist[b]:
		f = open (pwd + '/' + dirlist[b])
		acmkey = dirlist[b].replace('.txt', '')
		value = f.read().split()

		features = []

		# adding the location of the words
		q = 0
		while ((q < len(value)) and (value[q] != '--A')):
			features.append ([acmkey, value[q], 'Title'])
			q = q + 1
		while ((q < len(value)) and (value[q] != '--B')):
			features.append ([acmkey, value[q], 'Abstract'])
			q = q + 1  
		while ((q < len(value)) and (value[q] != '--R')):
			features.append ([acmkey, value[q], 'Body'])
			q = q + 1
		while ((q < len(value)) and (value[q] != '--TR')):
			features.append ([acmkey, value[q], 'Reference'])
			q = q + 1
		while ((q < len(value)) and (value[q] != '--CTR')):
			features.append ([acmkey, value[q], 'TR'])
			q = q + 1
		while q < len(value):
			features.append ([acmkey, value[q], 'CTR'])
			q = q + 1

		# natural language pre-processing
		pos = pos_tag(value)
		for j in range (0,len(value)):
			value[j] = re.sub("[^a-zA-Z]", "", value[j])
			value[j] = value[j].lower()
			if value[j] in docs.keys():
				docs[value[j]] += 1
			else:
				docs.update({value[j]:1})
			features[j][1] = value[j]
			features[j].append (pos[j][1])
			try: 
				if (keyphrase[features[j][1]] == 1):
					features[j].append ('yes')
			except:
				features[j].append ('no')

		# prepare text
		t = " ".join(value)

		# clean
		words = t.split()
		wordsclean = [w for w in words if not w in stopwords.words("english")]
		wordsclean = [w for w in wordsclean if len(w) > 2]
		l = [w for w in features if w[1] in wordsclean]

		# pad sections with null values for crf++
		q = 0
		l.insert (q, [acmkey, '0', '0', '0', 0.0, 0.0, 'no'])
		q = q + 1
		l.insert (q, [acmkey, '0', '0', '0', 0.0, 0.0, 'no'])
		q = q + 1
		l.insert (q, [acmkey, '0', '0', '0', 0.0, 0.0, 'no'])
		q = q + 1
		while ((q < len(l)) and (l[q][2] == 'Title')):
			q = q + 1
		if q == len(l):
			l.append ([acmkey, '0', '0', '0', 0.0, 0.0, 'no'])
			l.append ([acmkey, '0', '0', '0', 0.0, 0.0, 'no'])
			l.append ([acmkey, '0', '0', '0', 0.0, 0.0, 'no'])
		else:
			l.insert (q, [acmkey, '0', '0', '0', 0.0, 0.0, 'no'])
			q = q + 1
			l.insert (q, [acmkey, '0', '0', '0', 0.0, 0.0, 'no'])
			q = q + 1
			l.insert (q, [acmkey, '0', '0', '0', 0.0, 0.0, 'no'])
			q = q + 1
		while ((q < len(l)) and (l[q][2] == 'Abstract')):
			q = q + 1
		if q == len(l):
			l.append ([acmkey, '0', '0', '0', 0.0, 0.0, 'no'])
			l.append ([acmkey, '0', '0', '0', 0.0, 0.0, 'no'])
			l.append ([acmkey, '0', '0', '0', 0.0, 0.0, 'no'])
		else:
			l.insert (q, [acmkey, '0', '0', '0', 0.0, 0.0, 'no'])
			q = q + 1
			l.insert (q, [acmkey, '0', '0', '0', 0.0, 0.0, 'no'])
			q = q + 1
			l.insert (q, [acmkey, '0', '0', '0', 0.0, 0.0, 'no'])
			q = q + 1
		while ((q < len(l)) and (l[q][2] == 'Body')):
			q = q + 1
		if q == len(l):
			l.append ([acmkey, '0', '0', '0', 0.0, 0.0, 'no'])
			l.append ([acmkey, '0', '0', '0', 0.0, 0.0, 'no'])
			l.append ([acmkey, '0', '0', '0', 0.0, 0.0, 'no'])
		else:
			l.insert (q, [acmkey, '0', '0', '0', 0.0, 0.0, 'no'])
			q = q + 1
			l.insert (q, [acmkey, '0', '0', '0', 0.0, 0.0, 'no'])
			q = q + 1
			l.insert (q, [acmkey, '0', '0', '0', 0.0, 0.0, 'no'])
			q = q + 1
		while ((q < len(l)) and (l[q][2] == 'Reference')):
			q = q + 1
		if q == len(l):
			l.append ([acmkey, '0', '0', '0', 0.0, 0.0, 'no'])
			l.append ([acmkey, '0', '0', '0', 0.0, 0.0, 'no'])
			l.append ([acmkey, '0', '0', '0', 0.0, 0.0, 'no'])
		else:
			l.insert (q, [acmkey, '0', '0', '0', 0.0, 0.0, 'no'])
			q = q + 1
			l.insert (q, [acmkey, '0', '0', '0', 0.0, 0.0, 'no'])
			q = q + 1
			l.insert (q, [acmkey, '0', '0', '0', 0.0, 0.0, 'no'])
			q = q + 1
		while ((q < len(l)) and (l[q][2] == 'TR')):
			q = q + 1
		if q == len(l):
			l.append ([acmkey, '0', '0', '0', 0.0, 0.0, 'no'])
			l.append ([acmkey, '0', '0', '0', 0.0, 0.0, 'no'])
			l.append ([acmkey, '0', '0', '0', 0.0, 0.0, 'no'])
		else:
			l.insert (q, [acmkey, '0', '0', '0', 0.0, 0.0, 'no'])
			q = q + 1
			l.insert (q, [acmkey, '0', '0', '0', 0.0, 0.0, 'no'])
			q = q + 1
			l.insert (q, [acmkey, '0', '0', '0', 0.0, 0.0, 'no'])
			q = q + 1
		while ((q < len(l)) and (l[q][2] == 'CTR')):
			q = q + 1
		if q == len(l):
			l.append ([acmkey, '0', '0', '0', 0.0, 0.0, 'no'])
			l.append ([acmkey, '0', '0', '0', 0.0, 0.0, 'no'])
			l.append ([acmkey, '0', '0', '0', 0.0, 0.0, 'no'])
		else:
			l.insert (q, [acmkey, '0', '0', '0', 0.0, 0.0, 'no'])
			q = q + 1
			l.insert (q, [acmkey, '0', '0', '0', 0.0, 0.0, 'no'])
			q = q + 1
			l.insert (q, [acmkey, '0', '0', '0', 0.0, 0.0, 'no'])
			q = q + 1

		for q in range (0, len(l)):
			w = l[q]
			if (w[1] != '0'):
				n = w.pop(4)
				w.append(docs[w[1]])
				w.append(0)
				w.append(n)
				l[q] = w

		print ("%d l prepared for %s" % (count, acmkey))
		count = count + 1

		writer.writerows(l)

		# feature_matrix has features in the order:
		# acmkey, text, position, postag, keyphrase ('yes' or 'no')
# In[112]:

ff.close()

