__author__="Divine Gbagi"
__date__="8/31/20"
"""This program reads from the file mydata.txt to print the
    name, class and gpa in a line with a new line
    appearing for each name.
"""

from itertools import islice
from os.path import *
fName=input("Name of file: ")
if isfile(fName):
    with open(fName, 'r') as fObj:
        next_n_lines=list(islice(fObj, 2))
        while len(next_n_lines) !=0:
            lineList=next_n_lines
            if len(lineList)>1:
                name=lineList[0]; name=name[0:len(name)-1]
                tmpStr=lineList[1]
                tmpLineTwo=tmpStr.split(', ')
                course=tmpLineTwo[0]
                gpa=tmpLineTwo[1]; gpa=gpa[0:len(gpa)-1]
                print(name,course,gpa)
                next_n_lines=list(islice(fObj,2))
    fObj.close()
else:
    print("File doesn't exist")
