import pickle, os, csv
from math import log

ff = open("featuresnewmoreidf0.csv", "w")
gg = open("featuresnewmore0.csv", "r")

h = open("IDFdic.pckl", "rb")
dic = pickle.load(h)
h.close()

print ("Dictionary Loaded")

reader = csv.reader(gg)
writer = csv.writer(ff)

row = next(reader)
writer.writerow(row)

count = 1

curacm = "571841"
for row in reader:
	if row[0] != curacm:
		print ("%d %s doc completed" % (count, curacm))
		curacm = row[0]
		count += 1
	if (row[1] != "0_0"):
		row[4] = 1 + log(float(row[4]), 10)
		row[6] = log (2304 / dic[row[1]], 10)
	writer.writerow(row)

print ("%d %s doc completed" % (count, curacm))

gg.close()
ff.close()