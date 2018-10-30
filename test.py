from apriory import Apriori
from spreadsheet import *

data = getFromXml('menu.xlsx')
a = Apriori(data)
# print(a.frequency(data))
# print(a.search('onion','potato'))
item1 = a.itemSet(data)
print(a.isRepresentSameThing(item1))
print(a.isRepresentSameThing(a.itemSet(item1)))
# print(a.isRepresentSameThing(a.itemSet(data)))
# for key in item1:
#     if item1[key]==item2[key]:
#         print(key,"True")