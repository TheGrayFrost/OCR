import csv, pickle

ff = open("Unigram.csv", "r")
gg = open("UniramStyle.csv", "w")
h = open("style.pckl", "rb")

dic = pickle.load(h)

reader = csv.reader(ff)
writer = csv.writer(gg)

count = 0
curacm = "0"

for row in reader:
    if row[0] != curacm:
        print ("%d %s doc completed" % (count, curacm))
        curacm = row[0]
        count += 1
        if curacm in dic:
        	flag = 1
        	mb = dic[curacm][0]
        	mi = dic[curacm][1]
        	mbi = dic[curacm][2]
        else:
        	flag = 0

    if flag == 1:
    	if row[1] in mb:
    		row.insert(4, 'b')
    	elif row[1] in mi:
    		row.insert(4, 'i')
    	elif row[1] in mbi:
    		row.insert(4, 'bi')
    	else:
    		row.insert(4, 'n')
    	writer.writerow(row)

print ("%d %s doc completed" % (count, curacm))

ff.close()
gg.close()
h.close()