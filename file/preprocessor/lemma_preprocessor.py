from file.preprocessor.words_preprocessor import WordsPreprocessor
import nltk
from nltk.stem import WordNetLemmatizer

class LemmaPreprocessor(WordsPreprocessor):
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()

    def prepareWords(self, words: list):
        lemmatizedWords = []
        for word in words:
            lemmatizedWords.append(self.lemmatizer.lemmatize(word))
        return lemmatizedWords

