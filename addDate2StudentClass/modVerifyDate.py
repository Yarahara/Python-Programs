__author__="Divine Gbagi"
__date__="10/28/2020"
"""This program creates functions to test if a day, month, and year are valid
"""

from datetime import *
from calendar import *

def isValidYear(year):
    if year.isdigit() and int(year) >= MINYEAR and int(year) <=MAXYEAR:
        return True
    return False

def isValidMonth(month):
    if month.isdigit() and int(month) >=1 and int(month) <=12:
        return True
    return False

def isValidDay(year, month, theirDays):
    if theirDays.isdigit():
        res = monthrange(year, int(month))
        validNumDays = res[1]
        if int(theirDays) <= validNumDays and int(theirDays) >= 1:
            return True
    return False
   
def main( ):
    year = input("Please enter a number for the year: ")
    while isValidYear(year) == False:
        print("Error -- please enter a valid year ")
        year = input("Please enter a number for the year: ")
    year = int(year)
    month = input("Please enter a number for the month: ")
    while isValidMonth(month) == False:
        print("Error -- please enter a valid month ")
        month = input("Please enter a number for the month: ")
    month = int(month)
    day = input("Please enter a number for the day: ")
    while isValidDay(year, month, day) == False:
        print("Error -- please enter a valid day ")
        day = input("Please enter a number for the day: ")
    day = int(day)
    myDate = date(year, month, day)
    print(myDate)


