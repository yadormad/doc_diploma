from file.reader.file_reader import FileReader
from file.reader.txt_file_reader import TxtFileReader
from collections import Counter
import math

def getFileReaderByExtension(fileName) -> FileReader:
    fileExtension = fileName.split('.')[-1]
    if fileExtension == 'txt':
        return TxtFileReader()
    return -1

