#############################################
# Name: Divine-Favour Gbagi
# Submission Date: 04/09/2020
# Minnesota State University Moorhead
# Class: CSIS 152
# Assignment 12
#############################################

import random

def rand():
    numlist=[]
    while len(numlist) !=4:
        n=random.randint(0,9)
        if n not in numlist:
            numlist.append(n)
    return numlist

def main():
    print("Welcome to the Bulls and Cows Game. \n")
    number=rand()
    attempts=0
    choice= input("Enter a number: ")
    attempts +=1
    guess =[]
    for i in range (4):
        guess.append(int(choice[i]))
    while number !=guess:
        cows=0
        bulls=0
        for j in range(4):
            for o in range(4):
                if(guess[o] ==number[j] and o != j):
                    cows +=1
        for y in range (4):
            if guess [y] == number [y]:
                bulls +=1
        print("\n",bulls, " Bull",end=", ")
        print(cows, " Cow \n")
        guess=[]
        choice= input("Enter a number: ")
        attempts +=1
        for i in range (4):
            guess.append(int(choice[i]))
    print("You won after ", attempts, " guesses")


main()

