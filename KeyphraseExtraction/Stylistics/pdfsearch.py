import os
import linecache
import PyPDF2
import xml
from xml.dom import minidom
from nltk import word_tokenize, pos_tag
import re
from nltk.corpus import stopwords
import pickle

docs=os.listdir('/home/pourushsood/Desktop/pdfs')
#print docs
docstrue=[]
x=1
#for x in range (0,length(docs)):
try:
	with open('/home/pourushsood/Desktop/pdfs/'+docs[x]) as fp:
        		t=1
except IOError as err:
    	print "Error reading the file {0}: {1}".format(docs[x], err)

#pdf_toread = PdfFileReader('/home/pourushsood/Desktop/pdfs/'+docs[6])
#for x in range (0,len(docs)):
for x in range (0,len(docs)):
	# print x
	try:
		print x
		pdfFileObj = open('/home/pourushsood/Desktop/pdfs/'+docs[x], 'rb')
		pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
		pageObj = pdfReader.getPage(0)
		fpage=(pageObj.extractText())
		fpage=fpage.lower()
		#print fpage
		pdfFileObj.close()
		f=open('/home/pourushsood/Desktop/snlp/all_docs_abstacts_refined/'+docs[x][:-4]+'.txt','r')
		value = f.read().split()
		#prepare text
		t = " ".join(value)
		features=[]
		#print '\nhi'
		title= linecache.getline("/home/pourushsood/Desktop/snlp/all_docs_abstacts_refined/"+docs[x][:-4]+'.txt', 2)
		title= title[:-2]
		title=title.replace(' ','')
		title=title.lower()
		#print title
		if fpage.find(title)!=-1:
			docstrue.append(docs[x])
		else:
			print docs[x]
	except:
		pass
		#continue
print len(docstrue)
print len(docs)

to_remove=['title','body','abstract','references','future','work','citations','results','conclusion','acknowledgments','related']
#for x in range (0,len(docstrue)):
for x in range (0,len(docstrue)):
	print x
	url_input='/home/pourushsood/Desktop/pdfs/'+docstrue[x]
	#url_input='/home/pourushsood/Desktop/sparse.pdf'
	os.system ("cp %s /var/www/html/OCR++/myproject/media/documents/input.pdf" % url_input)
	os.chdir("/var/www/html/OCR++/myproject/media/documents/")
	#os.system ("pwd")
	os.system ("python main_script_batch.py")
		
	#h
	try:
		xmldoc = minidom.parse ("/var/www/html/OCR++/myproject/media/documents/input.xml")
	except:
		continue
	# replace above with the xml file address if you are working without ocr++

	#xmldoc = minidom.parse ("/var/www/html/OCR++/myproject/media/documents/input.xml")
	# get the text and related features
	itemlist = xmldoc.getElementsByTagName ("TOKEN")
	value = []
	att_tag=[]
	listoflist=[]
	att_tag_bold=[]
	att_tag_it=[]
	att_tag_bold_it=[]
	for i in range (0,len(itemlist)):
	    try:
	        value.append(itemlist[i].childNodes[0].nodeValue)
	    except:
	        continue
	    if itemlist[i].attributes['bold'].value == 'yes' and itemlist[i].attributes['italic'].value == 'yes':
			att_tag_bold_it.append(itemlist[i].childNodes[0].nodeValue)
	    elif itemlist[i].attributes['bold'].value == 'yes':
			att_tag_bold.append(itemlist[i].childNodes[0].nodeValue)
	    elif itemlist[i].attributes['italic'].value == 'yes':
			att_tag_it.append(itemlist[i].childNodes[0].nodeValue)
	    else:
			att_tag.append('none')
	# pre-process

	for j in range (0,len(att_tag_bold)):
		    att_tag_bold[j] = re.sub("[^a-zA-Z]", "", att_tag_bold[j])
		    att_tag_bold[j] = att_tag_bold[j].lower()
		    att_tag_bold[j] = str(att_tag_bold[j])
		    if att_tag_bold[j] in to_remove:
		    	att_tag_bold[j]=''
	att_tag_bold = list(filter(None, att_tag_bold))
	att_tag_bold = list(set(att_tag_bold))

	for j in range (0,len(att_tag_it)):
		    att_tag_it[j] = re.sub("[^a-zA-Z]", "", att_tag_it[j])
		    att_tag_it[j] = att_tag_it[j].lower()
		    att_tag_it[j] = str(att_tag_it[j])
		    if att_tag_it[j] in to_remove:
		    	att_tag_it[j]=''
	att_tag_it = list(filter(None, att_tag_it))
	att_tag_it = list(set(att_tag_it))

	for j in range (0,len(att_tag_bold_it)):
		    att_tag_bold_it[j] = re.sub("[^a-zA-Z]", "", att_tag_bold_it[j])
		    att_tag_bold_it[j] = att_tag_bold_it[j].lower()
		    att_tag_bold_it[j] = str(att_tag_bold_it[j])
		    if att_tag_bold_it[j] in to_remove:
		    	att_tag_bold_it[j]=''
	att_tag_bold_it = list(filter(None, att_tag_bold_it))
	att_tag_bold_it = list(set(att_tag_bold_it))

	# clean
	'''words = t.split()
	wordsclean = [w for w in words if not w in stopwords.words("english")]
	wordsclean = [w for w in wordsclean if len(w) > 2]
	featuresclean = [w for w in features if w[0] in wordsclean]'''

	#print att_tag_bold_it
	#print att_tag_bold
	#print att_tag_it
	listoflist.append((att_tag_bold,att_tag_it,att_tag_bold_it))
	#print listoflist
	fo=open( "/home/pourushsood/Desktop/snlp/outpdfs/"+docstrue[x][:-4]+".p", "wb" )
	pickle.dump( listoflist, fo )
	fo.close()