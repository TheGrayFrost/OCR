# OCR++
Code written for experimentation with reference tagging and keyphrase extraction from research papers.

Requirements CRF++ (>0.58) 



File Description for Keyphrase Extraction

Random Forest.ipynb: Contains code to train and evaluate random forest model 
                     on the stylistic bigram features finally extracted from the pdfs.

Folder: Scraper

paperlist.pckl contains the list of the papers in the dataset. (Found at http://disi.unitn.it/~krapivin/)
ACM Query.py runs a query on the paper doi's on the ACM Website. 
scraper.py, scr2.py scrape those pdfs from CiteSeerX.
DOI.py, PDF.py, PDF List.py verify if the pdfs are the ones we expected.

Folder: Feature Generation

FGen.py, Feature Generate.py, FinalFG.py generate features for Unigram Model
BiIDF.py, BiIDFNew.py generate IDF's for Bigrams
BiFG.py, BiFGNew.py, BiFinalFG.py generate features for Bigram Model

Folder: Stylistics

dicgen.py, key.py, setgen.py, tfidfdicgen.py generate and store the word-int map required for random forests 
(as scikit learn random forests can only work with numbers)
pdfsearch.py, style.py extract stylistic features from pdfs and save them
styleadduni.py adds stylistics fetaures to unigram feature matrix
styleaddbi.py adds stylistic features to bigram feature matrix


