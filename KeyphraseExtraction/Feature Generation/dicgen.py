import pickle, os

pwd = os.getcwd()
dirlist = os.listdir(pwd + '/Sets')

count = 1

x = set()
dic = dict()

for b in dirlist:
    if ".pckl" in b:
        count += 1    
        f = open (pwd + "/Sets/" + b, 'rb')
        y = pickle.load(f)
        f.close()
        for el in y:
            if el in x:
                dic[el] += 1
            else:
                x.add(el)
                dic[el] = 1
        print ("%d %s set merged" % (count, b))

g = open ("settot.pckl", "wb")
pickle.dump (x, g)
g.close

h = open ("dictot.pckl", "wb")
pickle.dump (dic, h)
h.close