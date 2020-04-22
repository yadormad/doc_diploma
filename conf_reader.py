from file.preprocessor.preprocessor_combiner import PreprocessorCombiner
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

def getClassifierByConf(conf):
    if('rf' in conf):
        return RandomForestClassifier()
    if ('kn' in conf):
        return KNeighborsClassifier()

class ConfReader:
    def __init__(self, confPath='config.txt'):
        file = open(confPath, 'r', encoding='utf-8')
        lines = file.read().split('\n')
        self.preprocCombiner = PreprocessorCombiner(lines[0])
        self.useIdf = int(lines[1]) == 1
        self.trainCsv = lines[2]
        self.testCsv = lines[3]
        self.classifier = getClassifierByConf(lines[4])
