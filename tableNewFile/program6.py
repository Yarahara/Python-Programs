__author__="Divine Gbagi"
__date__="10/19/2020"
"""This program reads from a file to make a table out of an employee's
    ID, their first name,their last name, their birthdate, their age,
    their date of hire, and their salary.
    This program also writes the names of employees over 60 years old, along
    with the names of employees who have a salary above 50000 or have worked
    for the company more than 20 years into a new file.
"""
#Importing the necessary module needed to do math with dates
from datetime import *
#Importing the necessary module needed to read and write from a file
from os.path import *

#Finds the difference in time in terms of years between today and the hiredate
#after converting the hiredate into a date object
def yearsWorked(hireDate):
    hdList = hireDate.split("-")
    hireDateObj = date(int(hdList[2]),int(hdList[0]),int(hdList[1]))
    curDate=date.today()
    yearsEmployed= curDate- hireDateObj
    return yearsEmployed.days//365

#Provides the calculation to find the age of the employee after turning
#the birthdate into a date object
def calcAge(birthDate):
    bdList = birthDate.split("-")
    birthDateObj = date(int(bdList[2]),int(bdList[0]),int(bdList[1]))
    curDate=date.today()
    daysAlive= curDate- birthDateObj
    return daysAlive.days//365

#Produces an organized table for the employee (ID, First Name, Last Name,
#Birth Date, Age, Hire Date, Yrs Worked and Salary)
def printReport(empRoster):
    #Gives the heading
    print("{:>50s}".format("Employee Roster"))
    print('{0:<6s}{1:15s}{2:15s}{3:20s}{4:<11s}{5:20s} {6:<16s}{7:12s}'\
              .format("ID","First Name","Last Name", "Birth Date",\
                                              "Age", "Hire Date", "Yrs Worked",\
                                              "Salary"))
    #Keeps count of the sublist being worked on
    ct=0
    #Goes through the master list and figues out the employee's
    #ID, First Name, Last Name, Birth Date, Age, Hire Date, Yrs Worked
    #and prints it in a table form under the heading
    for element in empRoster:
        iD=empRoster[ct][0]
        firstName=empRoster[ct][1]
        lastName = empRoster[ct][2]
        eAge = calcAge(empRoster[ct][3])
        yrsWorked = yearsWorked(empRoster[ct][4])
        bdList = empRoster[ct][3].split("-")
        birthDate = date(int(bdList[2]),int(bdList[0]),int(bdList[1]))
        birthDate = datetime.strftime(birthDate, "%b %d, %Y")
        hdList = empRoster[ct][4].split("-")
        hireDate = date(int(hdList[2]),int(hdList[0]),int(hdList[1]))
        hireDate=datetime.strftime(hireDate, "%b %d, %Y")
        salary=empRoster[ct][5]
        ct += 1
        print('{0:<6s}{1:15s}{2:15s}{3:20s}{4:<11d}{5:20s} {6:<16d}{7:12s}'\
              .format(iD,firstName,lastName, birthDate,\
                                              eAge, hireDate, yrsWorked,\
                                              salary))

#Opens a file that exists and reads it then removes the new line
#but if the file doesn't exist it returns an empty list
def openFile():
    #Asks the user for a file name
    fName=input("Enter file name: ")
    eInfo = []
    #Checks if the file exists and runs it if it does
    if isfile(fName):
        fObj=open(fName, "r")
        eInfo = fObj.readlines()
        #Takes the new line character out of the program
        for index in range(len(eInfo)):
            eInfo[index] = eInfo[index].rstrip('\n').split(", ")
        fObj.close()
    return eInfo

#Concatenates the employees over 60, employees who make more than 50000
#, employees who have worked over 20 years into one master string
#so it can be written into a new file
def writtenInfo(empRoster):
    #Makes a heading string starting with the heading so names can be added
    #to it.
    ageStr = "Employees over 60 years old: " + "\n"
    salaryStr = "\nEmployees over 60 years old: " + "\n"
    loyaltyStr = "\nEmployees that have worked for the company more than 20 years"\
                 "\n"
    #Goes through empRoster the master list and finds the years worked,
    #salary and age so it can add the name of the employee who
    #meets the requirements in the heading to the heading string
    for smallList in empRoster:
        firstName = smallList[1]
        lastName = smallList[2]
        salary = smallList[5]
        yrsWorked = yearsWorked(smallList[4])
        age = calcAge(smallList[3])
        #Checks if the conditions for the heading string is met and then
        #concatenates it to the corresponding heading string.
        if age > 60:
            ageStr += firstName +" "+ lastName + "\n"
        if int(salary) > 50000:
            salaryStr += firstName + " "+ lastName + "\n"
        if yrsWorked > 20:
            loyaltyStr += firstName + " "+ lastName + "\n"
    #Combines all the string into one master string so it can go through
    #the .write function.
    masterStr = ageStr + salaryStr + loyaltyStr
    return masterStr

#Allows the user to name a file to write the information in the
#writtenInfo function into it
def writeInFile(aString):
    wFile=input("What should the text file be named: ")
    newFile=open(wFile, "w")
    newFile.write(aString)
    newFile.close()

#Uses all the functions together in a simplified form to be run
def main():
    empRoster = openFile()
    if empRoster != []:
        printReport(empRoster)
        empInfoStr = writtenInfo(empRoster)
        writeInFile(empInfoStr)       
    else:
        print("Nonexistent file")

#Calls the main function so it can run
main()
        
