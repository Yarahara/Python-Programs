__author__="Divine Gbagi"
__date__="10/12/2020"
"""This program tells you the occurence of words in a file
"""

from os.path import *
import string

#Creates a function that reads from the file
def readTheFile(fName):
    wordList = []
    fObj=open(fName, "r")
    line = fObj.readline()
    
    #Removes the punctuation in the line, makes the line a list called
    #lineList, adds the line in  lineList to the list called wordList then
    #closes the file after iterating through each line in the file
    while line:
        line = removePunc(line)
        lineList = line.split()
        wordList += lineList
        line = fObj.readline()
    fObj.close()
    return wordList

#Creates a function that removes punctuation from a string  
def removePunc(aString):
    
    #Replaces each punctuation in the string with an empty space
    for ch in aString:
        if ch in string.punctuation:
            aString = aString.replace(ch,"")
    return aString

#Creates a function that makes a dictionary out of a list that has words
def createDict(listOfWords, myDict):

    #Keeps a tally of the number of times a word is in the list of words
    for elm in listOfWords:
        if elm.lower() not in myDict:
            myDict[elm.lower()] = 1
        else:
            myDict[elm.lower()] += 1
    #print(myDict)

#Displays the word and it's occurence in the file in the format of a table        
def printReport(myDict):

    #Prints the heading
    print("{:<20s}{:>s}".format("Word","Occurence"))

    #Prints the word to the left and prints the word's occurence to the right
    for key in myDict:
        print("{:<20}{:>}".format(key, myDict[key]))
    
#Calls all the functions above to produce a table that shows a word and its
#occurence
def main():
    fName=input("Enter the name of file: ")

    #Calls the functions above if the name of the file fName exists so the
    #program can run it
    if isfile(fName):
        words = readTheFile(fName)
        myDict = {}
        createDict(words,myDict)
        printReport(myDict)
    else:
        print("Nonexistent file")
    

main()
