from file.preprocessor.words_preprocessor import WordsPreprocessor
from file.reader.file_reader import FileReader
from file.vectorizator.file_vectorizator import FileVectorizator
from os import listdir
from os.path import isdir, join
import nltk

from file.util import getFileReaderByExtension

class FilesReader:
    def __init__(self, wordsPeprocessors: list, fileVectorizator: FileVectorizator, directory: str):
        self.wordsPeprocessors = wordsPeprocessors
        self.fileVectorizator = fileVectorizator
        self.directory = directory
        self.fileNames = []

    def readAndPrepareFiles(self):
        classes = [dir for dir in listdir(self.directory) if isdir(join(self.directory, dir))]
        for className in classes:
            classPath = join(self.directory, className)
            for fileName in listdir(classPath):
                self.fileNames.append(fileName)
                fileReader: FileReader = getFileReaderByExtension(fileName)
                # todo parallel
                fileText = fileReader.readFile(join(classPath, fileName))
                # write output???
                wordsList = nltk.tokenize.word_tokenize(fileText)
                for wordsPeprocessor in self.wordsPeprocessors:
                    wordsList = wordsPeprocessor.prepareWords(wordsList)
                self.fileVectorizator.vectorizeFile(className, wordsList)
