__author__="Divine Gbagi"
__date__="11/04/2020"
"""This program creates a class for vehicle with a child class called car
"""
from datetime import * 
class Vehicle:
    __numVehicles = 0
    __nextVinToUse = 1000
    
    def __init__(self, tmpYear, tmpColor):
        self.__VIN = Vehicle.__nextVinToUse
        self.__year = tmpYear
        self.__color = tmpColor
        Vehicle.__numVehicles += 1
        Vehicle.__setVIN()

    def getNumVehicles(self):
        return Vehicle.__numVehicles

    def getVIN(self):
        return self.__VIN

    def __setVIN():
        Vehicle.__nextVinToUse += 153

    def getIsNew(self):
        curYear = date.today().year
        if self.__year  == curYear:
            return True
        else:
            return False
        
    def getYearManufactured(self):
        return self.__year

    def getColor(self):
        return self.__color

    def calcVehicleAge(self):
        curYear = date.today().year
        age = curYear - self.__year
        return age

    def __str__(self):
        tmp = "Year: " + str(self.getYearManufactured()) + "\n"
        tmp += "Color: " + self.getColor() + "\n"
        tmp += "New: " + str(self.getIsNew()) +"\n"
        tmp += "Vehicle age: " + str(self.calcVehicleAge()) + "\n"
        tmp += "VIN: " + str(self.getVIN()) +"\n"
        return tmp

class Car(Vehicle):
    __numHondas = 0

    def __init__(self, tmpYr, tmpColor, tmpMake):
        Vehicle.__init__(self,tmpYr,tmpColor)
        self.__make = tmpMake
        if self.__make == "Honda":
            Car.__numHondas +=1

    def getMake(self):
        return self.__make

    def getNumHondas(self):
        return Car.__numHondas

    def __str__(self):
        tmp = Vehicle.__str__(self)
        tmp += "\n" + "Make: " + self.getMake()
        tmp += "\n" + "Number of Hondas: " + str(self.getNumHondas())
        return tmp

    
        
    
    
