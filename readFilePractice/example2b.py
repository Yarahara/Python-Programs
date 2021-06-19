__author__="Divine Gbagi"
__date__="8/31/20"
"""This program reads from the file myData.txt and prints each of the characters
    in the file down a line in its own line.
"""

import os.path
fileName=input("Name of the text file: ")
if os.path.isfile(fileName):
    myFileObj = open(fileName, "r")
    charList=myFileObj.read()
    print("List of Characters in the File: ", charList)
    for ch in charList:
        print(ch)
    myFileObj.close()
else:
    print("File ", fileName, " not found")
