#from modAccountV1 import *
#from modAccountV2 import *
from modAccountV3 import *

def main():
    a1 = Account("WellsFargo", "Checking", 6000)
    print(a1)
    print("The updated balance is: ", a1.calcInterest())

    ID = a1.getAcctID()
    bank = a1.getBank()
    acctType = a1.getType()
    bal = a1.getBalance()
    print("ID is: ", ID)
    print("Bank name is: ", bank)
    print("Account Type is: ", acctType)
    print("Balance is: ", bal)
    print(ID, bank, acctType, bal, "\n")

    a1.setBank("Chase")
##    a1.setType("401k")
    a1.setBalance(6500)
    print(a1)    

    a2 = Account("TCF", "Savings", 7000)
    print(a2)

    ID = a2.getAcctID()
    bank = a2.getBank()
    acctType = a2.getType()
    bal = a2.getBalance()
    print("ID is: ", ID)
    print("Bank name is: ", bank)
    print("Account Type is: ", acctType)
    print("Balance is: ", bal)
    print(ID, bank, acctType, bal, "\n")

    a2.setBank("Affinity")
##    a2.setType("Mortgage")
    a2.setBalance(6500)
    print(a2)

main()
