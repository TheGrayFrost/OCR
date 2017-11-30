import csv, pickle

ff = open("BigramNum.csv", "r")
gg = open("BigramStyle.csv", "w")
h = open("style.pckl", "rb")
u = open("StyleNum.pckl", "wb")

dic = pickle.load(h)

reader = csv.reader(ff)
writer = csv.writer(gg)

count = 0
counts = 0
curacm = "0"
row = next(reader)
b = row
b.insert(4, 'Style')
writer.writerow(b)

StyDic = {}

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
		w = row[1].split('_')
		if w[0] in mb:
			SA = 'b'
		elif w[0] in mi:
			SA = 'i'
		elif w[0] in mbi:
			SA = 'bi'
		else:
			SA = 'n'

		if w[1] in mb:
			SB = 'b'
		elif w[1] in mi:
			SB = 'i'
		elif w[1] in mbi:
			SB = 'bi'
		else:
			SB = 'n'

		S = SA + '_' + SB
		if S not in StyDic:
			StyDic[S] = counts
			counts += 1
		row.insert(4, StyDic[S])
		writer.writerow(row)

print ("%d %s doc completed" % (count, curacm))

pickle.dump(StyDic, u)
u.close()
ff.close()
gg.close()
h.close()