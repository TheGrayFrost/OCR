# OCR++
Code written for experimentation with reference tagging and keyphrase extraction from research papers.

Requirements CRF++ (>0.58) 

##Code Description for Reference extraction

Steps for Running the code

We have train and test data in Trainbatch.txt and Testbatch.txt.
We use a CRF++ to train our model.

Also provided are 3 template files for training the model:
a. Using Only POS Tags
b. Using POS Tags and Stylistic Features
c. Using POS Tags and Stylsitic Features( Double weightage to POS Tags)

To train a model:
 
	crf_learn <template_file_name> TrainBatch.txt <tagger_model_name>

To test a model:
	
	crf_test -m <tagger_model_name> TestBatch.txt -> <outputfilename.txt>

To check Accuracy of model:

	python accuracy.py <outputfilename.txt>



##File Description for Keyphrase Extraction

###Random Forest.ipynb: Contains code to train and evaluate random forest model 
                     on the stylistic bigram features finally extracted from the pdfs.

###Folder: Scraper

paperlist.pckl contains the list of the papers in the dataset. (Found at http://disi.unitn.it/~krapivin/)
ACM Query.py runs a query on the paper doi's on the ACM Website. 
scraper.py, scr2.py scrape those pdfs from CiteSeerX.
DOI.py, PDF.py, PDF List.py verify if the pdfs are the ones we expected.

###Folder: Feature Generation

FGen.py, Feature Generate.py, FinalFG.py generate features for Unigram Model
BiIDF.py, BiIDFNew.py generate IDF's for Bigrams
BiFG.py, BiFGNew.py, BiFinalFG.py generate features for Bigram Model

###Folder: Stylistics

dicgen.py, key.py, setgen.py, tfidfdicgen.py generate and store the word-int map required for random forests 
(as scikit learn random forests can only work with numbers)
pdfsearch.py, style.py extract stylistic features from pdfs and save them
styleadduni.py adds stylistics fetaures to unigram feature matrix
styleaddbi.py adds stylistic features to bigram feature matrix


