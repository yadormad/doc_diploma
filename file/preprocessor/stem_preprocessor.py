from file.preprocessor.words_preprocessor import WordsPreprocessor
from nltk.stem.snowball import SnowballStemmer

class StemPreprocessor(WordsPreprocessor):
    def __init__(self):
        self.stemmer = SnowballStemmer("russian") 

    def prepareWords(self, words: list):
        return [self.stemmer.stem(word) for word in words]