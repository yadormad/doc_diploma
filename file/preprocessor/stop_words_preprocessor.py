from file.preprocessor.words_preprocessor import WordsPreprocessor
from nltk.corpus import stopwords

class StopWordsPreprocessor(WordsPreprocessor):
    def __init__(self):
        self.stop_words = stopwords.words('english')

    def prepareWords(self, words: list):
        return [i for i in words if ( i not in self.stop_words )]