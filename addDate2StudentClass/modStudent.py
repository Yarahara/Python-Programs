__author__="Divine Gbagi"
__date__="10/28/2020"
"""This program creates a class for student with the attributes
    name, id, major and gpa
"""
from datetime import *

class Student:
    def __init__(self,studentName, ID, major,birthDate):
        self._name = studentName
        self._ID = ID
        self._major = major
        self._birthDate = birthDate
        self.date = date

    def getStudentName(self):
        return self._name

    def setStudentName(self,newStudentName):
        self._name = newStudentName

    def getID(self):
        return self._ID

    def setID(self,newID):
        self._ID = newID

    def getMajor(self):
        return self._major

    def setMajor(self,newMajor):
        self._major = newMajor

    def getBirthDate(self):
##        dateList = self._birthDate.split(", ")
##        birthDate = date(int(dateList[0]), int(dateList[1]), int(dateList[2]))
        birthDate = datetime.strftime(self._birthDate, "%b %d, %Y")
        return birthDate

    def setBirthDate(self,newBirthDate):
        self._birthDate = newBirthDate 
  
    def calcAge(self):
##        dateList = self._birthDate.split(", ")
##        #daysPerYear = 365.2425                    #self._birthdate = "1374, 6, 7" has to be splitted
##        birthDate = date(int(dateList[0]), int(dateList[1]), int(dateList[2]))
        age = (date.today() - self._birthDate).days // 365 
        return age

    def __str__(self):
        tmp = ""
        tmp += "Name: " + self._name +"\n"\
               "ID: " + str(self._ID) + "\n"\
               "Major: " + self._major + "\n"\
               "Birth Date: " + Student.getBirthDate(self) + "\n"\
               "Age: " + str(Student.calcAge(self)) + "\n"
        return tmp
