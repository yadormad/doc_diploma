import numpy as np

class fCounter:
    def __init__(self, originClasses, predictedClasses):
        self.originClasses = originClasses
        self.predictedClasses = predictedClasses
        classesSet = set(originClasses)
        classesSet.update(predictedClasses)
        self.classesList = list(classesSet)
        self.countConfusionMatrix()
        print('fCounter initialized')
    
    def countPrecision(self, className):
        classIndex = self.classesList.index(className)
        denominator = 0
        for i in self.confusionMatrix[classIndex]:
            denominator += i
        return self.confusionMatrix[classIndex][classIndex] / denominator
        
    def countRecall(self, className):
        classIndex = self.classesList.index(className)
        denominator = 0
        for i in self.confusionMatrix:
            denominator += i[classIndex]
        return self.confusionMatrix[classIndex][classIndex] / denominator

    def countConfusionMatrix(self):
        self.confusionMatrix = np.zeros((len(self.classesList), len(self.classesList)))
        for predictedClass, originClass in zip(self.predictedClasses, self.originClasses):
            self.confusionMatrix[self.classesList.index(predictedClass)][self.classesList.index(originClass)] += 1
    
    def countAvgPrecision(self):
        sumPrecision = 0
        for className in self.classesList:
            sumPrecision += self.countPrecision(className)
        return sumPrecision / len(self.classesList)

    def countAvgRecall(self):
        sumRecall = 0
        for className in self.classesList:
            sumRecall += self.countRecall(className)
        return sumRecall / len(self.classesList)

    def countF(self):
        precision = self.countAvgPrecision()
        print('precision calculated')
        recall = self.countAvgRecall()
        print('recall calculated')
        return 2 * precision * recall / (precision + recall)