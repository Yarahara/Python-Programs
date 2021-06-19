__author__="Divine Gbagi"
__date__="8/31/20"
"""This program reads from the file myData.txt and says, "Student" before
    the name, "had a GPA of" followed by the float number next to the name
    to essentialy tell the GPA of the student in the file myData.txt in 2 lines
"""

import os.path
fileName = input("Name of text file: ")
if os.path.isfile(fileName):
    with open(fileName)as myFileObj:
        for line in myFileObj:
            oneStu=line.split(' ')
            print('Student', oneStu[0], oneStu[1], 'had a GPA of', oneStu[2])
else:
    print("File ", fileName, " not found")
