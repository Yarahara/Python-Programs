__author__="Divine Gbagi"
__date__="8/31/20"
"""This program reads from the file myData.txt and prints the first and last name
    in the file after the word Student and the number in the file after the word
    GPA and makes the sentence, "Student {first and last name in file" had a GPA
    of {number in file}. for name in a new line"
"""

import os.path
fileName=input("Name of the text file: ")
if os.path.isfile(fileName):
    myFileObj=open(fileName,"r")
    lineList=myFileObj.readlines()
    for line in lineList:
        stuList = line.split()
        print('Student', stuList[0], stuList[1], 'had a GPA of', stuList[2])
        myFileObj.close()
else:
    print("File ", fileName, " not found")
        
