#############################################
# Name: Divine-Favour Gbagi
# Submission Date: 04/21/2020
# Minnesota State University Moorhead
# Class: CSIS 152
# Assignment 13
#############################################

def sum_of_even_num (start, end):
    thesum=0
    if start >= end:
        return 0
    else:
        while start < end:
            if start % 2 ==0:
                thesum += start
            start +=1
        return thesum

print("sum_of_even_num (1, 10) =", sum_of_even_num (1, 10))
print("sum_of_even_num (1, 1) =", sum_of_even_num (1, 1))
print("sum_of_even_num (2, 2) =", sum_of_even_num (2, 2))
print("sum_of_even_num (5, 2) =", sum_of_even_num (5, 2))

def sum_of_squares_of_even_num (start, end):
    thesum=0
    if start >= end:
        return 0
    else:
        while start <end:
            if start %2==0:
                thesum+=start**2
            start +=1
        return thesum

print("sum_of_squares_of_even_num (1, 10) =", sum_of_squares_of_even_num (1, 10))
print("sum_of_squares_of_even_num (1, 1) =", sum_of_squares_of_even_num (1, 1))
print("sum_of_squares_of_even_num (2, 2) =", sum_of_squares_of_even_num (2, 2))
print("sum_of_squares_of_even_num (5, 2) =", sum_of_squares_of_even_num (5, 2))


    

