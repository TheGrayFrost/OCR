import pickle, os, csv

ff = open("featuresnewless0.csv", "r")
gg = open("featuresnewmore0.csv", "w")

reader = csv.reader(ff)
writer = csv.writer(gg)

idfdic = {}

count = 1

curacm = "571841"
h = open("./Bigrams/" + curacm + "dic.pckl")
bidic = pickle.load(h)
for word in bidic:
    if word in idfdic:
        idfdic[word] += 1
    else:
        idfdic[word] = 1
h.close()
print ("%d %s tfdic completed" % (count, curacm))

row = next(reader)
writer.writerow(row)

for row in reader:
    if row[0] != curacm:
        print ("%d %s doc completed" % (count, curacm))
        curacm = row[0]
        count += 1
        bidic.clear()
        h = open("./Bigrams/" + curacm + "dic.pckl")
        bidic = pickle.load(h)
        for word in bidic:
            if word in idfdic:
                idfdic[word] += 1
            else:
                idfdic[word] = 1
        h.close()
        print ("%d %s tfdic completed" % (count, curacm))
    if (row[1] != "0_0"):
        row[4] = bidic[row[1]]
    writer.writerow(row)


print ("%d %s doc completed" % (count, curacm))
h = open("IDFdic.pckl", "wb")
pickle.dump(idfdic, h)
h.close()

print ("idfdic saved")

gg.close()
ff.close()