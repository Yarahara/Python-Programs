myDict = {'Math': 81, 'Physics': 83, 'Chemistry':87}
newList = []
for key in myDict:
    newList.append((key, myDict[key]))
numStuList = []
finalList = []
for key in myDict:
    numStuList.append(myDict[key])
numStuList.sort(reverse = True)
for num in numStuList:
    for major in newList:
        if num == major[1]:
            finalList.append(major)
print(finalList)
