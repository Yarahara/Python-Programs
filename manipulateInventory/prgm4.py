__author__="Divine Gbagi"
__date__="09/29/2020"
""" This program presents the user with a menu and lets them choose
    to add to an ID, description, price and quantity to an inventory,
    to sort the iventory by quantity, to display the iventory by printing
    the inventory with the total cost appended to each item and a
    grand total printed at the bottom.
"""
from os.path import *

def createMenu(listOfChoices, menuTitle):
    num=1
    str1="\n"
    
    for choice in listOfChoices:
        str1 += str(num) + str(". ") + choice + "\n"
        num +=1
        
    return menuTitle + str1

def getValidChoice(numChoices, menuStr):
    print(menuStr)
    question=input("Enter your choice: ")
    while (question.isdigit()== False) or int(question) <1\
          or int(question) >numChoices:
        print("Error-- invalid choice please try again. \n")
        print(menuStr)
        question=input("Enter your choice: ")
    return int(question)

def addProduct(prodDict):
    aID=int(input("Enter id: "))
    aDesc=input("Enter description: ")
    aUnitPrice=float(input("Enter unit price: "))
    aQuantity=int(input("Enter quanity: "))
    prodDict[aID]=[aDesc, aUnitPrice, aQuantity]

def printReport(prodDict):
    fmt="{0:<7.0f}{1:30s}${2:<29.2f}{3:<24.0f}${4:<.2f}"
    print("{:^100} \n".format("Product Roster"))
    print("{:<7s}{:30s}{:30s}{:24s}{:27s}"\
          .format("ID", "Description","Unit Price", "Quantity", "TotalCost"))
    print("="*100)

    tot=0
    for iD in prodDict:
        empInfo = prodDict[iD]
        des = empInfo[0]
        unitPrice = empInfo[1]
        quant = empInfo[2]
        totCost = unitPrice * quant
        tot +=totCost
        print(fmt.format(iD, des, unitPrice, quant, totCost))
    
    print("\nGrand Total: $"+str(tot) + "\n")

def openFile(fName, newDict):
    
    
        fObj=open(fName, "r")
        stock=fObj.readline()
        while stock:
            nStock=stock.rstrip('\n')
            #print(nStock)
            sStock=nStock.split(", ")
            #print(sStock)
            newDict[int(sStock[0])]= [sStock[1], float(sStock[2]), \
                                      int(sStock[3])]
            
            stock=fObj.readline()
        fObj.close()
    

def sorting(newDict):
    quanList=[]
    for k, valList in newDict.items():
        quan = valList[2]
        quanList.append(quan)
    #print(quanList)
    quanList.sort()
    #print(quanList)
    aDict=dict()
    for quan in quanList:
        for k, valList in newDict.items():
            if valList[2] == quan:
                aDict[k] = valList
    printReport(aDict)

def main():
    fName=input("Enter the name of the file: ")
    if isfile(fName):
        empDict={}
        openFile(fName, empDict)
        #print(empDict)
        nMenu=["Add product", "Sort by quantity (low to high)", \
               "Print Inventory",\
               "Quit"]
        
        menuStr= createMenu(nMenu, "Menu")
        ch=getValidChoice(len(nMenu), menuStr)
        while ch != len(nMenu):
            if ch == 1:
                addProduct(empDict)
            if ch == 2:
                sorting(empDict)
            if ch == 3:
                printReport(empDict)
            ch=getValidChoice(len(nMenu), menuStr)
        print("Thank you. You're done.")
    else:
        print("Error --no such file-- cannot be read")
        
        
main()

