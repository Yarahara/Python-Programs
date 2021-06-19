__author__="Divine Gbagi"
__date__="8/31/20"
"""This program reads from the file mydata.txt and prints the result
    a list.
"""

from itertools import islice
from os.path import *
fName = input("Name of file: ")
if isfile(fName):
    with open(fName,'r') as fObj:
        next_n_lines=list(islice(fObj,2))
        while len(next_n_lines)!=0:
            lineList=next_n_lines
            print(lineList)
            next_n_lines=list(islice(fObj,2))
    fObj.close()
else:
    print("File doesn't exist")
              
