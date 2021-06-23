#############################################
# Name: Divine-Favour Gbagi
# Submission Date: 03/06/2020
# Minnesota State University Moorhead
# Class: CSIS 152
# Assignment 10
#############################################

def isleapYear(y):
    if y%4 !=0:
        return "False it is a common year"
    elif y%100 !=0:
        return "True it is a leap year"
    elif y%400 !=0:
        return "False it is a common year"
    else:
        return "True it is a leap year"
    

def main():
    year=int(input("What year is it? "))
    print(isleapYear(year))
    
main()

