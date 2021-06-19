__author__="Divine Gbagi"
__date__="8/31/20"
"""This program reads from the file myData.txt to tell you the first
    15 characters in the file after saying "List of 15 characters from the file
    and then printing each of the 15 characters in the file one by one in a line.
"""

import os.path
fileName=input("Name of the text file: ")
if os.path.isfile(fileName):
    myFileObj=open(fileName,"r")
    charList=myFileObj.read(15)
    print("List of 15 characters from the file: ", charList)
    for ch in charList:
        print(ch)
    myFileObj.close()
else:
    print("File", fileNmae, " not found")
