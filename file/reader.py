from file.preprocessor.words_preprocessor import WordsPreprocessor
from file.vectorizator.file_vectorizator import FileVectorizator
from os import listdir
from os.path import isdir, join
import nltk
from threading import Thread


class Reader:
    def __init__(self, wordsPeprocessors: list, fileVectorizator: FileVectorizator, values):
        self.wordsPeprocessors = wordsPeprocessors
        self.fileVectorizator = fileVectorizator
        self.values = values

    def readAndPrepareFiles(self):
        for (i, [className, fileText]) in enumerate(self.values):
            tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
            wordsList = tokenizer.tokenize(str(fileText).replace('\\', ' '))
            for wordsPeprocessor in self.wordsPeprocessors:
                wordsList = wordsPeprocessor.prepareWords(wordsList)
            self.fileVectorizator.vectorizeFile(className, wordsList)
            print("{} readed".format(i))
            self.entries = i + 1
