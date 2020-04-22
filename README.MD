installing dependencies:
pip install -r requirements.txt

run:
python main.py <config file path optionally>

config.txt:

ngram-1-2 sw lem stem
1
corpus\csv\train_min.csv
testData\csv\test_min.csv
kn

1 line - preprocessor sequence
[ngram-1-2] - ngram preprocessor with range from 1 to 2
[sw] - stopwords
[lem] - lemmatizer
[stem] - stemmer

2 line - use idf <1> if true <0> if false
3 line - train data csv file
4 line - test data csv file
5 line - classifier
[kn] - KNeighbors
[rf] - RandomForest