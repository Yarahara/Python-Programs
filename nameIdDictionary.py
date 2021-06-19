#1
empDict={}
uID=input("Enter your ID and name: ")
section=uID.split()
empDict[section[0]]=section[1]
print(empDict)

#3
cName=input("Enter a name: ")
done=False
for key in empDict:
    if cName==empDict[key]:
        done=True
        print(key)
if done == False:
    print("Name not found")

#4
cID=input("Enter an ID: ")
if cID in empDict:
    del empDict[cID]
else:
    print("No delete - ID not found")

#5
enterID=input("Enter an ID: ")
if enterID in empDict:
    name=input("Enter a newFullName: ")
    empDict[enterID]=name
print(empDict)

#6
empDict={"ID": "Name","123":"Joe Brown","235":"Molly Smith"}
for key in empDict:    
    print(key, "\t", empDict[key])

#----------list----------------
    #1
empList=[]
ein=input("Enter your ID and name: ")
#2
ein.split()
empList.append(ein[0])
empList.append(ein[1])

#3
en=input("Enter a name: ")
if en == empList[1]:
    print(empList[0])
else:
    print("Name not found")
#4
ei=input("Enter a ID: ")
if ei in empList:
    del empList[0:]
else:
    print("No delete - name not found")

#5
ei2=input("Enter an ID: ")
if ei2 in empList:
    newFullName=input("Enter a new full name: ")
    empList[1]=newFullName
else:
    print("No such ID exists")

#6
print("ID \t Name \n123\tJoe Brown\n235\tMary Smith)



    
    

