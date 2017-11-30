import re, os
from nltk import word_tokenize, pos_tag
from nltk.corpus import stopwords
from math import log

pwd = os.getcwd()
dirlist = os.listdir(pwd)

feature_matrix = []

#for filename in dirlist:
for b in range(0, 10):
    if ".txt" in dirlist[b]:
        f = open (pwd + '/' + dirlist[b])
        x = dirlist[b].replace ('.txt', '.key')
        m = open (pwd + '/' + x)
        value = f.read().split()
        keyphrase = m.read().split()

        features = []

        # adding the location of the words
        q = 0
        while ((q < len(value)) and (value[q] != '--A')):
            features.append ([value[q], 'Title'])
            q = q + 1
        while ((q < len(value)) and (value[q] != '--B')):
            features.append ([value[q], 'Abstract'])
            q = q + 1  
        while ((q < len(value)) and (value[q] != '--R')):
            features.append ([value[q], 'Body'])
            q = q + 1
        while ((q < len(value)) and (value[q] != '--TR')):
            features.append ([value[q], 'Reference'])
            q = q + 1
        while ((q < len(value)) and (value[q] != '--CTR')):
            features.append ([value[q], 'TR'])
            q = q + 1
        while q < len(value):
            features.append ([value[q], 'CTR'])
            q = q + 1

        # natural language pre-processing
        pos = pos_tag(value)
        for j in range (0,len(value)):
            value[j] = re.sub("[^a-zA-Z]", "", value[j])
            value[j] = value[j].lower()
            features[j][0] = value[j]
            features[j].append (pos[j][1])
            if features[j][0] in keyphrase:
                features[j].append ('yes')
            else:
                features[j].append ('no')

        # prepare text
        t = " ".join(value)

        # clean
        words = t.split()
        wordsclean = [w for w in words if not w in stopwords.words("english")]
        wordsclean = [w for w in wordsclean if len(w) > 2]
        featuresclean = [w for w in features if w[0] in wordsclean]


        # remove duplicates and find tf
        l = []
        c = []
        for w in featuresclean:
            if w not in l:
                l.append(w)
                c.append(featuresclean.count(w))

        i = 0
        for w in l:
            r = 1 + log(c[i], 10)
            w.append(r)
            i = i + 1


        # pad sections with null values for crf++
        q = 0
        l.insert (q, ['0', '0', '0', 0.0, 0.0, 'no'])
        q = q + 1
        l.insert (q, ['0', '0', '0', 0.0, 0.0, 'no'])
        q = q + 1
        l.insert (q, ['0', '0', '0', 0.0, 0.0, 'no'])
        q = q + 1
        while ((q < len(l)) and (l[q][1] == 'Title')):
            q = q + 1
        if q == len(l):
            l.append (['0', '0', '0', 0.0, 0.0, 'no'])
            l.append (['0', '0', '0', 0.0, 0.0, 'no'])
            l.append (['0', '0', '0', 0.0, 0.0, 'no'])
        else:
            l.insert (q, ['0', '0', '0', 0.0, 0.0, 'no'])
            q = q + 1
            l.insert (q, ['0', '0', '0', 0.0, 0.0, 'no'])
            q = q + 1
            l.insert (q, ['0', '0', '0', 0.0, 0.0, 'no'])
            q = q + 1
        while ((q < len(l)) and (l[q][1] == 'Abstract')):
            q = q + 1
        if q == len(l):
            l.append (['0', '0', '0', 0.0, 0.0, 'no'])
            l.append (['0', '0', '0', 0.0, 0.0, 'no'])
            l.append (['0', '0', '0', 0.0, 0.0, 'no'])
        else:
            l.insert (q, ['0', '0', '0', 0.0, 0.0, 'no'])
            q = q + 1
            l.insert (q, ['0', '0', '0', 0.0, 0.0, 'no'])
            q = q + 1
            l.insert (q, ['0', '0', '0', 0.0, 0.0, 'no'])
            q = q + 1
        while ((q < len(l)) and (l[q][1] == 'Body')):
            q = q + 1
        if q == len(l):
            l.append (['0', '0', '0', 0.0, 0.0, 'no'])
            l.append (['0', '0', '0', 0.0, 0.0, 'no'])
            l.append (['0', '0', '0', 0.0, 0.0, 'no'])
        else:
            l.insert (q, ['0', '0', '0', 0.0, 0.0, 'no'])
            q = q + 1
            l.insert (q, ['0', '0', '0', 0.0, 0.0, 'no'])
            q = q + 1
            l.insert (q, ['0', '0', '0', 0.0, 0.0, 'no'])
            q = q + 1
        while ((q < len(l)) and (l[q][1] == 'Reference')):
            q = q + 1
        if q == len(l):
            l.append (['0', '0', '0', 0.0, 0.0, 'no'])
            l.append (['0', '0', '0', 0.0, 0.0, 'no'])
            l.append (['0', '0', '0', 0.0, 0.0, 'no'])
        else:
            l.insert (q, ['0', '0', '0', 0.0, 0.0, 'no'])
            q = q + 1
            l.insert (q, ['0', '0', '0', 0.0, 0.0, 'no'])
            q = q + 1
            l.insert (q, ['0', '0', '0', 0.0, 0.0, 'no'])
            q = q + 1
        while ((q < len(l)) and (l[q][1] == 'TR')):
            q = q + 1
        if q == len(l):
            l.append (['0', '0', '0', 0.0, 0.0, 'no'])
            l.append (['0', '0', '0', 0.0, 0.0, 'no'])
            l.append (['0', '0', '0', 0.0, 0.0, 'no'])
        else:
            l.insert (q, ['0', '0', '0', 0.0, 0.0, 'no'])
            q = q + 1
            l.insert (q, ['0', '0', '0', 0.0, 0.0, 'no'])
            q = q + 1
            l.insert (q, ['0', '0', '0', 0.0, 0.0, 'no'])
            q = q + 1
        while ((q < len(l)) and (l[q][1] == 'CTR')):
            q = q + 1
        if q == len(l):
            l.append (['0', '0', '0', 0.0, 0.0, 'no'])
            l.append (['0', '0', '0', 0.0, 0.0, 'no'])
            l.append (['0', '0', '0', 0.0, 0.0, 'no'])
        else:
            l.insert (q, ['0', '0', '0', 0.0, 0.0, 'no'])
            q = q + 1
            l.insert (q, ['0', '0', '0', 0.0, 0.0, 'no'])
            q = q + 1
            l.insert (q, ['0', '0', '0', 0.0, 0.0, 'no'])
            q = q + 1

        feature_matrix.append(l)

        # feature_matrix has features in the order:
        # text, position, postag, keyphrase ('yes' or 'no'), tf

        print (b)

# add idf after processing all documents
m = len (feature_matrix)

for fi in feature_matrix:
    for w in fi:
        if w[0] != '0':
            count = 0
            for a in feature_matrix:
                for x in a:
                    if ((w[0] == x[0]) and (w[2] == x[2])):
                        count = count + 1
                        break
            s = log(m/count, 10)
            w.append(s)
            n = w.pop(3)
            w.append (n) 

# feature_matrix now has features in the order:
# text, position, postag, tf, idf, keyphrase ('yes' or 'no')


matr = open ('/Users/GrayFrost/Desktop/NLPTP/train.txt', 'a')
for x in range (0, len(feature_matrix)):
    for y in range (0, len(feature_matrix[x])):
        for z in range (0, len(feature_matrix[x][y])):
            matr.write(str(feature_matrix[x][y][z]))
            matr.write("  ")
        matr.write("\n")


