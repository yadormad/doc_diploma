from file.preprocessor.words_preprocessor import WordsPreprocessor
from file.reader.file_reader import FileReader
from file.vectorizator.file_vectorizator import FileVectorizator
from os import listdir
from os.path import isdir, join
import nltk
import csv
from threading import Thread

from file.util import getFileReaderByExtension

class CsvReader:
    def __init__(self, wordsPeprocessors: list, fileVectorizator: FileVectorizator, directory: str):
        self.wordsPeprocessors = wordsPeprocessors
        self.fileVectorizator = fileVectorizator
        self.directory = directory
        self.fileNames = []
        self.entries = 0

    def readAndPrepareFiles(self):
        with open(self.directory, 'r', encoding='utf-8') as File: 
            readed = csv.reader(File, delimiter=',', quotechar='"')
            for (i, [className, _, fileText]) in enumerate(readed):
                # thread = RecordProcessorThread(self.wordsPeprocessors, self.fileVectorizator, fileText, className, self.directory, i)
                # thread.start()
                tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
                wordsList = tokenizer.tokenize(fileText.replace('\\', ' '))
                for wordsPeprocessor in self.wordsPeprocessors:
                    wordsList = wordsPeprocessor.prepareWords(wordsList)
                self.fileVectorizator.vectorizeFile(className, wordsList)
                print("{} readed {}".format(self.directory, i))
                self.entries = i + 1


class RecordProcessorThread(Thread):
    def __init__(self, wordsPeprocessors: list, fileVectorizator: FileVectorizator, fileText, className, directory, i):
        Thread.__init__(self)
        self.wordsPeprocessors = wordsPeprocessors
        self.fileVectorizator = fileVectorizator
        self.fileText = fileText
        self.className = className
        self.directory = directory
        self.i = i

    def run(self):
        wordsList = nltk.tokenize.word_tokenize(self.fileText)
        for wordsPeprocessor in self.wordsPeprocessors:
            wordsList = wordsPeprocessor.prepareWords(wordsList)
        self.fileVectorizator.vectorizeFile(self.className, wordsList)
        print("{} readed {}".format(self.directory, self.i))