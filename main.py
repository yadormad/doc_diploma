from file.csv_reader import CsvReader
from file.vectorizator.tf_idf_vectorizator import TfIdfVectorizator
from sklearn.metrics import accuracy_score
from f_measure import fCounter
from conf_reader import ConfReader

from sklearn.ensemble import RandomForestClassifier
import sys

def compute(X_test, Y_test, X_predict, classifier):
    classifier.fit(X_test, Y_test)
    pred = classifier.predict(X_predict)
    return pred

def main(argv):
    if (len(argv) > 0):
        confReader = ConfReader(argv[0])
    else:
        confReader = ConfReader()
    
    trainingSampleReader = CsvReader(
        confReader.preprocCombiner.generatePreprocArray(),
        TfIdfVectorizator(confReader.useIdf),
        confReader.trainCsv,
    )

    testDataReader = CsvReader(
        confReader.preprocCombiner.generatePreprocArray(),
        TfIdfVectorizator(confReader.useIdf),
        confReader.testCsv
    )

    trainingSampleReader.readAndPrepareFiles()

    print('training prepared')

    testDataReader.readAndPrepareFiles()

    print('test data prepared')

    testDataReader.fileVectorizator.wordSet = trainingSampleReader.fileVectorizator.wordSet

    X_trained, C_trained = trainingSampleReader.fileVectorizator.getMatrex()

    print('training matrix')

    X_test, C_test = testDataReader.fileVectorizator.getMatrex()

    print('test matrix')

    C_predicted = compute(X_trained, C_trained, X_test, confReader.classifier)

    print('prediceted')

    print ('accuracy:')

    print(accuracy_score(C_test, C_predicted))

    print ('f-measure:')

    print(fCounter(C_test, C_predicted).countF())

if __name__ == "__main__":
   main(sys.argv[1:])