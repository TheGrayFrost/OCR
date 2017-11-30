import pickle

s = open('doc2doi.pckl', 'rb')
t = open('doinew.pckl', 'rb')

f = pickle.load(s)
dn = pickle.load(t)

newd = []
newf = {}
for key in f:
	if key in dn:
		newd.append([key, dn[key], f[key]])
	else:
		newf[key] = f[key]

print ("Docs to download: ", len(newd), sep = '')
print ("Docs to doi ", len(newf), sep = '')

u = open('doc2downew.pckl', 'wb')
v = open('doc2doinew.pckl', 'wb')
pickle.dump(newd, u)
pickle.dump(newf, v)

