#lab11 -- Two designs for a class
#design 1
class Student:
    __nextID = 100
    __numStudents = 0

    def __init__(self, tmpName, tmpMajor, tmpGPA): # id is NOT passed in!
        id = Student.__nextID; Student.__nextID += 10
        Student.__numStudents += 1
        self.__listStuInfo = [id, tmpName, tmpMajor, tmpGPA] #ONLY ONE ATTRIBUTE-a LIST

    def getID(self):
        return self.__listStuInfo[0] # no setter for the ID!
    
    def getName(self):
        return self.__listStuInfo[1]

    def setName(self, newName):
        self.__listStuInfo[1] = newName

    def getMajor(self):
        return self.__listStuInfo[2]

    def setMajor(self, newMajor):
        self.__listStuInfo[2] = newMajor

    def getGPA(self):
        return self.__listStuInfo[3]

    def setGPA(self, newGPA):
        self.__listStuInfo[3] = newGPA

    def __str__(self):
        tmp = str(self.getID()) + "\n" + self.getName() + "\n" + \
              self.getMajor() + "\n" + str(self.getGPA()) + "\n"
        return tmp

    def getNumStudents():
        return Student.__numStudents

    
