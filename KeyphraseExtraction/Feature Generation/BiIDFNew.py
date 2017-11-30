import pickle, os, csv

ff = open("featuresnewless0.csv", "r")
gg = open("featuresnewmore0.csv", "w")

reader = csv.reader(ff)
writer = csv.writer(gg)

count = 1

curacm = "571841"
h = open("./Bigrams/" + curacm + "dic.pckl")
bidic = pickle.load(h)
h.close()

row = next(reader)
row = ["ACM Key", "Word", "Zone", "POS Tag", "TF1", "TF2", "IDF1", "IDF2", "Label"]
writer.writerow(row)

for row in reader:
    if row[0] != curacm:
        print ("%d %s doc completed" % (count, curacm))
        curacm = row[0]
        count += 1
        bidic.clear()
        h = open("./Bigrams/" + curacm + "dic.pckl")
        bidic = pickle.load(h)
        h.close()
    if (row[1] != "0_0"):
        row[4] = bidic[row[1]]
    writer.writerow(row)


print ("%d %s doc completed" % (count, curacm))

gg.close()
ff.close()