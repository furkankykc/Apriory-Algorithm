import pandas as pd



def getFromXml(dir):
    data = pd.read_excel(dir)
    data = data.to_dict()

    for key in data:
        temp = []
        for i in range(len(data[key])):
            temp.append(data[key][i])
        data[key] = temp

    # print(data)
    return data