#lab11 -- Two designs for a class
#design 2
class Student:
    __nextID = 100
    __numStudents = 0

    def __init__(self, tmpName, tmpMajor, tmpGPA): # id is NOT passed in!
        self.__ID = Student.__nextID; Student.__nextID += 10
        Student.__numStudents += 1
        self.__name = tmpName
        self.__major = tmpMajor
        self.__GPA = tmpGPA

    def getID(self):
        return self.__ID # no setter for the ID!
    
    def getName(self):
        return self.__name

    def setName(self, newName):
        self.__name = newName

    def getMajor(self):
        return self.__major

    def setMajor(self, newMajor):
        self.__major = newMajor

    def getGPA(self):
        return self.__GPA

    def setGPA(self, newGPA):
        self.__GPA = newGPA

    def __str__(self):
        tmp = str(self.getID()) + "\n" + self.getName() + "\n" + \
              self.getMajor() + "\n" + str(self.getGPA()) + "\n"
        return tmp

    def getNumStudents():
        return Student.__numStudents
