from math import log
from machine_learning_in_action_tuling.CH03 import treePlotter

def calShannonEnt(dataset):
    """
    计算给定数据集的熵
    :param dataset:数据集
    :return: 熵
    """
    numEntries = len(dataset)
    labelCounts = {}
    for featVec in dataset:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt


def createDataSet():
    dateSet = [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return dateSet, labels


def splitDataSet(dataSet, axis, value):
    """
    按照给定特征划分数据集
    :param dataSet: 数据集
    :param axis: 划分数据集的特征
    :param value: 需要返回的特征的值
    :return: 划分好的数据集
    """
    returnSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis + 1:])
            returnSet.append(reducedFeatVec)
    return returnSet


def chooseBestFeatureToSplit(dataset):
    """
    选择最好的数据集划分方式
    :param dataset:数据集
    :return:最好的特征值
    """
    numFeatures = len(dataset[0]) - 1
    baseEntropy = calShannonEnt(dataset)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataset]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataset, i, value)
            prob = len(subDataSet) / float(len(dataset))
            newEntropy += prob * calShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if infoGain > bestInfoGain:
            bestInfoGain = infoGain
            bestFeature = i
        return bestFeature


def majorityCnt(classList):
    """
    返回出现次数最多的标签
    :param classList: 标签
    :return:
    """
    classCount = {}
    for vote in classList:
        if vote not in classCount:
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.items(), key=lambda item: item[1], reverse=True)
    return sortedClassCount[0][0]


def createTree(dataset, labels):
    """
    创建树的代码3
    :param dataset:
    :param labels:
    :return:
    """
    classList = [example[-1] for example in dataset]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataset[0]) == 1:
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataset)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel: {}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataset]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataset, bestFeat, value), subLabels)
    return myTree





def classify(inputTree, featLabels, testVec):
    firstStr = [key for key in inputTree.keys()][0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    for key in secondDict.keys():
        if testVec[featIndex] == key:
            if type(secondDict[key]).__name__ == 'dict':
                classLabel = classify(secondDict[key], featLabels, testVec)
            else:
                classLabel = secondDict[key]
    return classLabel



def storeTree(inputTree, filename):
    import pickle
    fw = open(filename, 'wb+')
    pickle.dump(inputTree, fw)
    fw.close()


def grabTree(filename):
    import pickle
    fr = open(filename, 'rb+')
    return pickle.load(fr)





if __name__ == '__main__':
    # myDat, labels = createDataSet()

    # subDataSet = splitDataSet(myDat, 0, 1)
    # print(subDataSet)


    # print(chooseBestFeatureToSplit(myDat))

    # myTree = treePlotter.retrieveTree(0)
    # print(myTree)
    # print(classify(myTree, labels, [1, 0]))
    # print(classify(myTree, labels, [1, 1]))


    # storeTree(myTree, 'classifierStorage.txt')
    # print(grabTree('classifierStorage.txt'))


    fr = open('lenses.txt')
    lesens = [inst.strip().split('\t') for inst in fr.readlines()]
    lensesLabels = ['age', 'prescripe', 'astigmatic', 'tearRate']
    lensesTree = createTree(lesens, lensesLabels)
    print(lensesTree)
    treePlotter.createPlot(lensesTree)

