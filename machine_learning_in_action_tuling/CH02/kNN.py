import numpy as np
import matplotlib.pyplot as plt
from os import listdir

def createDataSet():
    group = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=lambda item: item[1], reverse=True)
    return sortedClassCount[0][0]


def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = np.zeros((numberOfLines, 3))
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0: 3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector


def scatterLegend(data, label, x, y):
    type1 = []
    type2 = []
    type3 = []
    for i in range(len(label)):
        if label[i] == 1:
            type1.append(np.array(data[i]))
        elif label[i] == 2:
            type2.append(np.array(data[i]))
        else:
            type3.append(np.array(data[i]))
    type1 = np.array(type1)
    type2 = np.array(type2)
    type3 = np.array(type3)
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    g1 = plt.scatter(type1[:, x], type1[:, y], c='r')
    g2 = plt.scatter(type2[:, x], type2[:, y], c='b')
    g3 = plt.scatter(type3[:, x], type3[:, y], c='k')
    plt.legend(handles=[g1, g2, g3], labels=['不喜欢', '魅力一般', '极具魅力'])
    plt.show()


def autoNorm(dataset):
    minVals = dataset.min(0)
    maxVals = dataset.max(0)
    ranges = maxVals - minVals
    normalDataSet = np.zeros(np.shape(dataset))
    m = dataset.shape[0]
    normalDataSet = dataset - np.tile(minVals, (m, 1))
    normalDataSet = normalDataSet / np.tile(ranges, (m, 1))
    return normalDataSet, ranges, minVals


def datingClassTest():
    hoRatio = 0.10
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    norMat, ranges, minvals = autoNorm(datingDataMat)
    m = norMat.shape[0]
    numTestVecs = int(m * hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classfierResult = classify0(norMat[i, :], norMat[numTestVecs: m, :], datingLabels[numTestVecs:m], 3)
        print("the classifierResult came back with: %d, the real answer is: %d" % (classfierResult, datingLabels[i]))
        if classfierResult != datingLabels[i]:
            errorCount += 1.0
    print("the totoal error rate is: %f" % (errorCount / float(numTestVecs)))


def classifyPerson():
    resultList = ['not at all', 'in small doses', 'in large doses']
    percentTats = float(input("percentage of time spent playing video games?"))
    ffMiles = float(input("frequent flier miles earned per year?"))
    iceCream = float(input("liters of ice cream consumed per year?"))
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    norMat, ranges, minvals = autoNorm(datingDataMat)
    inArr = np.array([percentTats, ffMiles, iceCream])
    classifierResult = classify0((inArr - minvals) / ranges, norMat, datingLabels, 3)
    print('You will probably like this person: ', resultList[classifierResult - 1])


def img2vector(filename):
    returnVector = np.zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVector[0, 32*i+j] = int(lineStr[j])
    return returnVector


def handwritingClassTest():
    hwLabels = []
    trainingFileList = listdir('digits/trainingDigits')
    m = len(trainingFileList)
    trainingMat = np.zeros((m, 1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i, :] = img2vector(f'digits/trainingDigits/{fileNameStr}')
    testFileList = listdir('digits/testDigits')
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('digits/testDigits/%s' % fileNameStr)
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        print("the classifierResult came back with: %d, the real answer is: %d" % (classifierResult, classNumStr))
        if classifierResult != classNumStr:
            errorCount += 1.0
    print("\nthe total number of errors is: %d" % errorCount)
    print("\nthe total error rate is: %f" % (errorCount/float(mTest)))


if __name__ == '__main__':
    # group, labels = createDataSet()
    # print(group)
    # print(labels)
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')

    # print(datingDataMat)
    # print(datingLabels[:20])
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2], 15.0*np.array(datingLabels), 15.0*np.array(datingLabels))
    # plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    # plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    # plt.xlabel('玩视频游戏所耗时间百分比')
    # plt.ylabel('每周消费的冰激凌公升数')
    # plt.show()

    # scatterLegend(datingDataMat, datingLabels, 0, 1)


    # norMat, ranges, minvals = autoNorm(datingDataMat)
    # print(norMat)
    # print(ranges)
    # print(minvals)


    # datingClassTest()


    # classifyPerson()

    # testVector = img2vector('digits/testDigits/0_13.txt')
    # print(testVector)

    handwritingClassTest()


