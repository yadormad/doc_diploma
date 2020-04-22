###installing dependencies:
``pip install -r requirements.txt``

###run:
``python main.py <config file path optionally>``

####config.txt:

ngram-1-2 sw lem stem<br/>
1<br/>
corpus\csv\train_min.csv<br/>
testData\csv\test_min.csv<br/>
kn


**1 line - preprocessor sequence<br/>**
[ngram-1-2] - ngram preprocessor with range from 1 to 2<br/>
[sw] - stopwords<br/>
[lem] - lemmatizer<br/>
[stem] - stemmer<br/>

**2 line - use idf <1> if true <0> if false<br/>**

**3 line - train data csv file<br/>**

**4 line - test data csv file<br/>**

**5 line - classifier<br/>**

[kn] - KNeighbors
[rf] - RandomForest
