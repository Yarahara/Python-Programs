__author__="Divine Gbagi"
__date__="09/11/2020"
"""This program checks to see if a choice made exists
"""

def CreateMenu(listOfChoices, menuTitle):
    num=1
    str1="\n"
    
    for choice in listOfChoices:
        str1 += str(num) + str(". ") + choice + "\n"
        num +=1
        
    return menuTitle + str1

def getValidChoice(numChoices, menuStr):
    #print(menuStr)
    question=input("Enter your choice: ")
    while (question.isdigit()== False) or int(question) <1\
          or int(question) >numChoices:
        print("Error-- invalid choice please try again. \n")
        print(menuStr)
        question=input("Enter your choice: ")
    return int(question)


chList=["Add", "Subtract", "Multiply",\
        "Divide", "Quit"]
menuStr=\
          CreateMenu(chList, "Main Menu")
print(menuStr)
ch=getValidChoice(len(chList),menuStr)

