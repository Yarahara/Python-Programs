from os.path import *

def isValidPhone(tmpPhone):
    digit="0123456789"
    p1=tmpPhone[0:3]
    p2=tmpPhone[4:7]
    p3=tmpPhone[8:]

    if len(tmpPhone) !=12:
        return [False, "Incorrect Length"]
    elif tmpPhone[3]!="-" or tmpPhone[7]!="-":
        return [False, "Hyphen missing"]
##    elif tmpPhone[7]!="-":
##        return [False, "Hyphen missing"]
    elif not p1.isdigit() or not p2.isdigit()\
         or not p3.isdigit():
        return[False, "All sections must be digits"]
##    elif p2[0] not in digit or p2[1] not in digit or p2[2] not in digit:
##        return[False, "Second section must be digits"]
##    elif p3[0] not in digit or p3[1] not in digit or p3[2] not in digit\
##         or p3[3] not in digit:
##        return[False, "Third section must be digits"]

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
