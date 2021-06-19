__author__="Divine Gbagi"
__date__="09/21/2020"
"""This program allows a user to choose from a menu to
    see their interest earned in their savings, savings
    balance, checkings balance, deposit to their checkings
    or withdraw from their checking.
"""

def createMenu(listOfChoices, menuTitle):
    num=1
    str1="\n"
    
    for choice in listOfChoices:
        str1 += str(num) + str(". ") + choice + "\n"
        num +=1
        
    return menuTitle + str1

def getValidChoice(numChoices, menuStr):
    question=input("Enter your choice: ")
    while (question.isdigit()== False) or int(question) <1\
          or int(question) >numChoices:
        print("Error-- invalid choice please try again. \n")
        print(menuStr)
        question=input("Enter your choice: ")
    return int(question)

def handleCheckMenu(checkBal, cMenuStr, numOptions):
    print("\n"+cMenuStr)
    chkChoice=getValidChoice(numOptions, cMenuStr)
    while chkChoice != numOptions:
        if chkChoice == 1:
            checkBal = deposit(checkBal)
        elif chkChoice == 2:
            checkBal = withdrawal(checkBal)
        elif chkChoice == 3:
            print("Your checking balance is ${0:,.2f}".format(checkBal))
        print("\n"+cMenuStr)
        chkChoice=getValidChoice(numOptions, cMenuStr)
    return checkBal

def deposit(checkBal):
    atmDeposit= float(input("What would you like to deposit? "))
    checkBal= atmDeposit + checkBal
    return checkBal

def withdrawal(checkBal):
    atmWithdrawal= float(input("What would you like to withdraw? "))
    if atmWithdrawal > checkBal:
        print("Withdrawal is not possible. Overdrafts not allowed.")
    else:
        checkBal= checkBal - atmWithdrawal
    return checkBal

def handleSavingsMenu(savBal, sMenuStr, numOptions):
    print("\n" + sMenuStr)
    savChoice=getValidChoice(numOptions, sMenuStr)
    while savChoice != numOptions:
        
        if savChoice == 1:
            savBal=calcInterest(savBal)
            
        elif savChoice == 2:
            displaySaveBalance(savBal)
        print("\n" + sMenuStr)    
        savChoice=getValidChoice(numOptions, sMenuStr)
    return savBal
                       
def calcInterest(savBal):
    interestEarned= savBal * 0.02
    savBal= savBal + interestEarned
    print("You've earned ${:.2f} in interest".format(interestEarned))
    return savBal

def displaySaveBalance(savBal):
    print("Your savings balance is ${:.2f}".format(savBal))
                  
def main():
    mainOptionList=["Savings", "Checking", "Quit"]
    savOptionList=["Display Interest Earned", "Display Savings Balance",\
                   "Back to Main"]
    chkOptionList=["Deposit", "Withdrawal", "Display Checking Balance",\
                    "Back to Main"]

    mainMenuStr=createMenu(mainOptionList, "Main Menu")
    savMenuStr=createMenu(savOptionList, "Savings Menu")
    chkMenuStr=createMenu(chkOptionList, "Checking Menu")

    print(mainMenuStr)

    savBal=100
    chkBal=0

    mainChoice=getValidChoice(len(mainOptionList), mainMenuStr)
    while mainChoice != len(mainOptionList):
        if mainChoice == 1:
            savBal = handleSavingsMenu(savBal, savMenuStr, len(savOptionList))
        elif mainChoice == 2:
            chkBal = handleCheckMenu(chkBal, chkMenuStr, len(chkOptionList))
        print("\n"+mainMenuStr)
        mainChoice=getValidChoice(len(mainOptionList), mainMenuStr)
    print("Exiting bank")
            


main()
            
            
