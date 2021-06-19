__author__="Divine Gbagi"
__date__="09/04/20"
"""I did the bonus. This program uses a function to tell if a phone number
    from a text file is valid or invalid.
"""
from os.path import *

def isValidPhone(tmpPhone):
    digit="0123456789"
    p1=tmpPhone[0:3]
    p2=tmpPhone[4:7]
    p3=tmpPhone[8:]
##    aP1=tmpPhone[1:4]
##    aP2=tmpPhone[5:8]                                               
##    aP3=tmpPhone[9:]

    if len(tmpPhone) !=12:
##        if len(tmpPhone)==13:
##            if tmpPhone[0] =="(" and tmpPhone[4]==")" and tmpPhone[8]=="-":
##                if aP1[0] in digit and aP1[1] in digit and aP1[2] in digit:
##                    if aP2[0] in digit and aP2[1] in digit and aP2[2] in digit:
##                        if aP3[0] in digit and aP3[1] in digit and aP3[2] in\
##                           digit:
##                            return [True, "Correct Format"]
##                
##                        else:
##                            return [False, "Third section must be digits"]
##                    else:
##                        return[False, "Second section must be digits"]
##                else:
##                    return[False, "First section must be digits"]
                
                        
                    
        return [False, "Incorrect Length"]
    elif not tmpPhone[3]=="-":
        return [False, "Hyphen missing"]
    elif not tmpPhone[7]=="-":
        return [False, "Hyphen missing"]
    elif p1[0] not in digit or p1[1] not in digit or p1[2] not in digit:
        return[False, "First section must be digits"]
    elif p2[0] not in digit or p2[1] not in digit or p2[2] not in digit:
        return[False, "Second section must be digits"]
    elif p3[0] not in digit or p3[1] not in digit or p3[2] not in digit\
         or p3[3] not in digit:
        return[False, "Third section must be digits"]

    else:
        return [True, "Correct Format"]


def convert(valid):
    if valid == "True":
        return "Yes"
    else:
        return "No"


def main():
    fName=input("Enter the name of the file: ")
    if isfile(fName):
        fObj=open(fName, "r")
        phNum=fObj.readline()
        print("{0:<27s}{1:24s}{2:27s}".format("Phone Number","Valid","Message"))
        print("="*80)
        while phNum:
            nPhNum=phNum.rstrip('\n')
            r=isValidPhone(nPhNum)
            r2=str(r[0])
            print('{0:<27s}{1:24s}{2:27s}'.format(nPhNum,convert(r2),r[1]))
            phNum=fObj.readline()
        fObj.close()
    else:
        print("Error --no such file-- cannot be read")

main()













                  
    
        
                
    
