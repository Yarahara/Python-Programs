d1 = {'a': 100, 'b': 200, 'c':300, 'e':90}
d2 = {'a': 30, 'b': 20, 'd':40, 'c':10}
comDict={}
for key in d1:
    if key in d2:
        tot = d1[key] + d2[key]
    else:
        tot = d1[key]
    comDict[key] = tot

for key in d2:
    if not key in d1:
        comDict[key] = d2[key]

print(comDict)
