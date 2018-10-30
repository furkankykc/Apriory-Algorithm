import numpy as np


class Apriori():
    def __init__(self, data):
        self.data = data
        self.treshold = 1 / 2 * len(data[next(iter(data))])

    def apriory(self, data):
        return self.isRepresentSameThing(self.selectSignificent(self.itemSet(data)))

    def frequency(self, data):
        frequency = {}
        for key in data:
            frequency[key] = (sum(data[key]))

        return frequency

    def selectSignificent(self, data):
        # frequency = self.frequency(data)
        temp = {}
        for key in data:

            if data[key] >= self.treshold:
                temp[key] = data[key]

        data = temp
        return data

    def itemSet(self, data):
        temp = {}
        for k in data:
            for l in data:
                if k != l:
                    # print(k, data[k], l, data[l])
                    # temp[k + '&' + l] = temp.get(k + '&' + l, 0) + 1
                    isContinue = True
                    if k + '&' + l.split('&')[-1] in data:
                        isContinue = False
                    if l.split('&')[-1] + '&' + k in data:
                        isContinue = False
                    for s in range(len(k.split('&')) - 1):
                        if k.split('&')[s] != l.split('&')[s]:
                            isContinue = False
                    if isContinue:
                        temp[k + '&' + l.split('&')[-1]] = int(sum(self.search(*k.split('&'), *l.split('&'))))
        return self.selectSignificent(temp)
        # return temp

    def isRepresentSameThing(self, data):
        temp = {}
        for key in data:
            isContinue = True
            tempSum = sum(bytearray(key.encode('utf8')))
            for l in temp:
                if sum(bytearray(l.encode('utf8'))) == tempSum:
                    isContinue = False
            if isContinue:
                temp[key] = data[key]

        return temp

    def listXor(self, list1, list2):
        temp = np.zeros(len(list1))
        for i in range(len(list1)):
            if (list1[i] == list2[i]) and list1[i] == 1:
                temp[i] = 1

        return temp

    def search(self, *args):
        temp = np.ones(len(self.data[next(iter(self.data))]))
        for key in args:
            temp = self.listXor(self.data[key], temp)
        return temp


if __name__ == '__main__':
    testData = {
        'apple': [1, 1, 0, 1],
        'pinapple': [0, 1, 1, 1],
        'pair': [0, 0, 0, 1],
        'melon': [1, 0, 0, 1],
        'cherry': [1, 0, 1, 1]
    }
    test = Apriori(testData)
    print(test.apriory(testData))
    print(test.apriory(test.apriory(testData)))
