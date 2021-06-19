'''find the highest 3 values in a dictionary that maps 
a studentID to a list of test score'''
myDict = {"111": [90,80,85],  "222":[70,79,65], "333":[83, 85, 89]}
newList = []
for key in myDict:
    for elm in myDict[key]:
        newList.append(elm)
newList.sort(reverse=True)
print(newList[:3])
        
