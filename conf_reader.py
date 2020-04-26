from file.preprocessor.preprocessor_combiner import PreprocessorCombiner
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
import pandas
import random

def getClassifierByConf(conf):
    if('rf' in conf):
        return RandomForestClassifier()
    if ('kn' in conf):
        return KNeighborsClassifier()
    if ('svm' in conf):
        return LinearSVC()

def readData(confLine):
    configArguments = confLine.split(' ')
    ext = configArguments[0].split('.')[-1]
    data = []
    if (ext == 'csv'):
        data = pandas.read_csv(configArguments[0], usecols=[int(configArguments[1]), int(configArguments[2])]).values
    if (ext == 'json'):
        data = pandas.DataFrame(pandas.read_json(configArguments[0], lines=True), columns=[configArguments[1], configArguments[2]]).values
    if (len(configArguments) > 3):
        data = random.choices(data, k=int(configArguments[3]))
    return data


class ConfReader:
    def __init__(self, confPath='config.txt'):
        file = open(confPath, 'r', encoding='utf-8')
        lines = file.read().split('\n')
        self.preprocCombiner = PreprocessorCombiner(lines[0])
        self.useIdf = int(lines[1]) == 1
        self.trainData = readData(lines[2])
        self.testData = readData(lines[3])
        self.classifier = getClassifierByConf(lines[4])
