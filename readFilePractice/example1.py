__author__="Divine Gbagi"
__date__="8/31/20"
"""This program reads from the file myData.txt to say the GPA of a student in
    the format of two lines after putting, "Student" in front of the name
    and, "had a GPA of" in front of the GPA.
"""

import os.path
fileName=input("Name of the text file: ")
if os.path.isfile(fileName):
    myFileObj=open(fileName, "r")
    for tmpLine in myFileObj:
        stuList=tmpLine.split()
        print('Student', stuList[0],stuList[1],'had a GPA of ', stuList[2])
    myFileObj.close()
else:
    print("File ", fileName," not found")
