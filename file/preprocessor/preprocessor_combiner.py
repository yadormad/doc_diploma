from file.preprocessor.stem_preprocessor import StemPreprocessor
from file.preprocessor.lemma_preprocessor import LemmaPreprocessor
from file.preprocessor.stop_words_preprocessor import StopWordsPreprocessor
from file.preprocessor.ngram_preprocessor import NgrammPreprocessor

def getPreprocByConf(conf):
    if('ngram' in conf):
        confAndParams = conf.split('-')
        return NgrammPreprocessor([int(confAndParams[1]), int(confAndParams[2])])
    if('sw' in conf):
        return StopWordsPreprocessor()
    if('lem' in conf):
        return LemmaPreprocessor()
    if('stem' in conf):
        return StemPreprocessor()

class PreprocessorCombiner:
    def __init__(self, confStr):
        self.confStr = confStr

    def generatePreprocArray(self):
        preprocArray = []
        for conf in self.confStr.split(' '):
            preprocArray.append(getPreprocByConf(conf))
        return preprocArray
