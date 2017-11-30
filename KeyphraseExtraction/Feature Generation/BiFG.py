import pickle, csv

ff = open("../featuresnewless0.csv", "w")
gg = open("../featuresmore0.csv", "r")


bidic = {}

reader = csv.reader(gg)
writer = csv.writer(ff)

count = 1

row = ["ACM Key", "Word", "Zone", "POS Tag", "TF1", "TF2" "IDF1", "IDF2", "Label"]
writer.writerow(row)

curacm = "571841"
row = [curacm, "0_0", "0_0", "0_0", 0, 0, 0, 0, "no_no"]
writer.writerow(row)
row1 = next(reader)
for row2 in reader:
	if (row1[0] == row2[0]):
		row = [row1[0], row1[1]+"_"+row2[1], row1[2]+"_"+row2[2], row1[3]+"_"+row2[3], 0, (float(row1[4])+ float(row2[4]))/2, 0, (float(row1[5])+ float(row2[5]))/2, row1[6]+"_"+row2[6]]
	else:
		row = [row1[0], "0_0", "0_0", "0_0", 0, 0, 0, 0, "no_no"]
		writer.writerow(row)
		row[0] = row2[0]
		print ("%d %s doc completed" % (count, curacm))
		h = open(curacm + "dic.pckl", "wb")
		pickle.dump(bidic, h)
		h.close()
		bidic.clear()
		print ("%d %s tf dic saved" % (count, curacm))
		curacm = row2[0]
		count += 1
	writer.writerow(row)
	row1 = row2
	if (row[1] != "0_0"):
		if row[1] in bidic:
			bidic[row[1]] += 1
		else:
			bidic[row[1]] = 1


print ("%d %s doc completed" % (count, curacm))
h = open(curacm + "dic.pckl", "wb")
pickle.dump(bidic, h)
h.close()
bidic.clear()
print ("%d %s tf dic saved" % (count, curacm))

gg.close()
ff.close()