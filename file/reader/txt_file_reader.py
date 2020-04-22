from file.reader.file_reader import FileReader

class TxtFileReader(FileReader):
    def readFile(self, path: str):
        file = open(path, 'r', encoding='utf-8')
        return file.read()
