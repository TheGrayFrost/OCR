import os
from itertools import islice
import pickle

dirlist=os.listdir("/Users/GrayFrost/Desktop/NLPTP/all_docs_abstacts_refined")

s = []
for i in range (0,len(dirlist)):
	if ".txt" in dirlist[i]:
		l = dirlist[i].replace(".txt", "")
		with open("/Users/GrayFrost/Desktop/NLPTP/all_docs_abstacts_refined/"+(dirlist[i])) as fin:
			for line in islice(fin, 1,2):
				s.append([l, line.replace(".\n", "")])

f = open('paperlist.pckl', 'wb')
pickle.dump(s, f)
f.close()


