__author__="Divine Gbagi"
__date__="10/28/2020"
"""This program creates a class for student with the attributes
    name, id, major and gpa, tests that class and uses modVerify program
    with the class
"""
from modStudent import *
from datetime import *
from modVerifyDate import *
def main():
    student11 = Student("Divine-Favour Gbagi",1234,"Computer Science", date(1999, 11, 19) )
    print(student11)

    s1 = Student("Ele Li",2134,"Business", date(1998, 12, 1) )
    print("Student 1: ", s1)
    print("Testing getters for Student 1")
    idNum = s1.getID(); print("ID Number: ", idNum)
    name = s1.getStudentName(); print("Name: ", name)
    major = s1.getMajor(); print("Major: ", major)
    birthDate = s1.getBirthDate(); print("Birth Date: ", birthDate)
    age = s1.calcAge(); print("Age: ", age)
    s2 = Student("Ben Jamin", 2121, "Economics", date(1997, 10, 13))
    print("\n\nStudent 2: ", s2)
    print("\nTesting setters for Student 2")
    s2.setStudentName("Jerry Smith")
    s2.setID(3001);
    s2.setMajor("Finance"), s2.setBirthDate(date(1996, 12, 15))
    print("Changing Student 2’s info to name Jerry Smith, id 3001, Major Finance, Birth Date 1996, 12, 15\n")
    print(s2)



    name = input("Enter name: ")
    ID = input("Enter ID: ")
    major = input("Enter major: ")
    birthYear = input("Enter birth year: ")
    year = isValidYear(birthYear)
    while year == False:
        birthYear = input("Enter birth year: ")
        year = isValidYear(birthYear)
    birthYear = int(birthYear)    
    birthMonth = input("Enter birth month: ")
    month = isValidMonth(birthMonth)
    while month == False:
        birthMonth = input("Enter birth month: ")
        month = isValidMonth(birthMonth)
    birthMonth = int(birthMonth)
    birthDay = input("Enter birth day: ")
    day = isValidDay(birthYear, birthMonth, birthDay)
    while day == False:
        birthDay = input("Enter birth day: ")
        day = isValidDay(birthYear, birthMonth, birthDay)
    birthDay = int(birthDay)
    s3= Student(name, ID, major, date(birthYear, birthMonth, birthDay))
    print(s3)

main()
    
