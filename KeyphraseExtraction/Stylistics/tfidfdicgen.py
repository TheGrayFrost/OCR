import csv, pickle

ff = open("Unigram.csv", "r")
h = open("TF-IDFdic.pckl", "wb")

dic = {}

reader = csv.reader(ff)

count = 1
curacm = "571841"
m = {}
for row in reader:
    if row[0] != curacm:
        dic[curacm] = m
        print ("%d %s doc completed" % (count, curacm))
        curacm = row[0]
        count += 1
        m = {}
    m[row[1]] = [row[4], row[5]]

dic[curacm] = m     
print ("%d %s doc completed" % (count, curacm))

pickle.dump (dic, h)
ff.close()
h.close()