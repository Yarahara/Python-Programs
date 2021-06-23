#############################################
# Name: Divine-Favour Gbagi
# Submission Date: 03/04/2020
# Minnesota State University Moorhead
# Class: CSIS 152
# Assignment 09
#############################################

def grade(x):
    if x>=90:
        return "A"
    if x<90 and x>=80:
        return "B"
    if x<80 and x>=70:
        return "C"
    if x<70 and x>=60:
        return "D"
    else:
        return "F"


def main():
    scores = [87, 92, 100, 54, 72, 84, 81, 74]
    for i in scores:
        print(grade(i))
    
main()
