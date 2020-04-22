from file.vectorizator.file_vectorizator import FileVectorizator
from sklearn.feature_extraction.text import TfidfVectorizer

class TfIdfVectorizator(FileVectorizator):
    def __init__(self, useIdf):
        self.wordSet = set()
        self.classesList = []
        self.corpus = []
        self.dictionaries = []
        self.useIdf = useIdf
    
    def vectorizeFile(self, className, words):
        self.wordSet.update(words)
        self.classesList.append(className)
        self.corpus.append(' '.join(map(str, words)))

    def getMatrex(self):
        vectorizer = TfidfVectorizer(vocabulary=self.wordSet, use_idf=self.useIdf)
        X = vectorizer.fit_transform(self.corpus)
        return X, self.classesList
