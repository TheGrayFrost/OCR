import pickle
import csv


ff = open("../featuresless0.csv", "r")
reader = csv.reader(ff)

count = 1

x = set()

curacm = "571841"
for row in reader:
    if (row[0] != curacm):
        f = open ("set" + curacm + ".pckl", "wb")
        pickle.dump (x, f)
        f.close
        print ("%d %s set generated" % (count, curacm))
        count += 1
        x.clear()
        curacm = row[0]
    else:
    	if (row[1] != '0'):
        	x.add(row[1])


f = open ("set" + curacm + ".pckl", "wb")
pickle.dump (x, f)
f.close
print ("%d %s set generated" % (count, curacm))
x.clear()

ff.close()