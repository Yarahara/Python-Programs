#############################################
# Name: Divine Gbagi
# Submission Date: 04/07/2020
# Minnesota State University Moorhead
# Class: CSIS 152
# Assignment 11
#############################################
def coursePoints(credits,grade):

    if grade =="A" or grade =="A+":
        points=credits*4.0
    elif grade =="A-":
        points= credits * 3.67
    elif grade =="B+":
        points= credits * 3.33
    elif grade =="B":
        points= credits * 3.00
    elif grade =="B-":
        points= credits * 2.67
    elif grade =="C+":
        points= credits * 2.33
    elif grade =="C":
        points= credits * 2.00
    elif grade =="C-":
        points= credits * 1.67
    elif grade =="D+":
        points= credits * 1.33
    elif grade =="D":
        points= credits * 1.00
    elif grade =="D-":
        points= credits * 0.67
    elif grade =="F+":
        points= credits * 0.33
    elif grade =="F":
        points= credits * 0.00
    return points
        

def report(numclass,totcredit,totGPA):
    print("Semester Summary ")
    print("courses taken: " + str(numclass))
    print("credits taken: " +str(totcredit))
    print("GPA points: " + str(totGPA))
    print("Semester GPA: " + str(round(totGPA/totcredit,2)))

def main():
    totGPA=0
    totcredit=0
    numclass=int(input("How many classes did you take? "))
    print()
    for cl in range(numclass):
        print("Class "+str(cl+1))
        credit=int(input("number of credits: "))
        grade=input("Grade: ")
        print()
        gpa= coursePoints(credit,grade)
        totGPA +=gpa
        totcredit +=credit

    report(numclass,totcredit,totGPA)
    
                   

main()
        
