from file.preprocessor.words_preprocessor import WordsPreprocessor
from nltk import ngrams

class NgrammPreprocessor(WordsPreprocessor):
    def __init__(self, n_range):
        self.n_range = n_range

    def prepareWords(self, words: list):
        ngramList = []
        for n in range(self.n_range[0], self.n_range[1] + 1):
            for gram in ngrams(words, n):
                ngramList.append(gram)
        return [ '_'.join(grams) for grams in ngramList]
