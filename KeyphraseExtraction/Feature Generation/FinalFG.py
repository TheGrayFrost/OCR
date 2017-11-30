import pickle, csv
from math import log


ff = open("featuresless0.csv", "r")
gg = open("featuresmore0.csv", "w")
hh = open("dictot.pckl", "rb")
dic = pickle.load(hh)
hh.close()
reader = csv.reader(ff)
writer = csv.writer(gg)

count = 1

curacm = "571841"
for row in reader:
	if (row[1] != '0'):
		row[4] = 1 + log(int(row[4]), 10)
		df = dic[row[1]]
		row[5] = log (2304/df, 10)
	writer.writerow(row)
	if (row[0] != curacm):
		print ("%d %s doc completed" % (count, curacm))
		curacm = row[0]
		count += 1

print ("%d %s doc completed" % (count, curacm))

gg.close()
ff.close()