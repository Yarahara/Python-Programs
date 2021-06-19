from datetime import *
from os.path import *

def main():
    fileName = input("Enter a filename: ")
    if isfile(fileName):
        tmpList = readFile(fileName)
        printReport(tmpList)
    else:
        print("Invalid filename")

def readFile(fName):
    fObj = open(fName, "r")
    lineList = fObj.readlines()
    ct = 0
    for line in lineList:
        line = line.rstrip("\n")
        lineList[ct] = line.split(", ")
        ct +=1
    fObj.close()
    return lineList

def printReport(tmpList):
    print("{0:<45}{1:<20}{2:<20s}".format("Title", "Publication Date",\
                                          "Alternate Date"))
    for tmp in tmpList:
        dateObj = datetime.strptime(tmp[1], "%m-%d-%Y")
        pubDate = datetime.strftime(dateObj, "%B %d, %Y")
        altDate = datetime.strftime(dateObj, "%m/%d/%y")
        print("{0:<45}{1:<20}{2:<20s}".format(tmp[0], pubDate, altDate))

main()
    
