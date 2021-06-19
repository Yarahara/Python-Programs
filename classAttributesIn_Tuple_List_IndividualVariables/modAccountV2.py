__author__="Divine Gbagi"
__date__="11/04/2020"
"""This program creates a class for account with the attributes
    bank, type, and balance as individual variables
"""


class Account:
    __nextAcctID = 1000

    def __init__(self, tmpBank, tmpType, tmpBalance):
        self.__acctID = Account.__nextAcctID
        self.__bank = tmpBank
        self.__type = tmpType
        self.__bal = tmpBalance
        Account.__setAcctID()

    def getAcctID(self):
        return self.__acctID 
    
    def getBank(self):
        return self.__bank

    def setBank(self, newBank):
        self.__bank = newBank

    def getType(self):
        return self.__type

    def setType(self, newType):
        self.__type = newType

    def getBalance(self):
        return self.__bal

    def setBalance(self, newBal):
        self.__bal = newBal

    def __setAcctID():
        Account.__nextAcctID +=173

    def calcInterest(self):
        s = Account.getType(self)
        if s.upper() == "CHECKING":
            newBalance = Account.getBalance(self) * 1.01
            Account.setBalance(self,newBalance)
        elif s.upper() == "SAVINGS":
            newBalance = Account.getBalance(self) * 1.02
            Account.setBalance(self,newBalance)
        return "{:.2f}".format(newBalance)

    def __str__(self):
        tmp = "Account ID: " + str(self.getAcctID()) + "\n"
        tmp += "Bank Name: " + self.getBank() + "\n"  
        tmp += "Account Type: " + self.getType() + "\n"
        tmp += "Balance: " + "$" + str(self.getBalance()) + "\n"
        return tmp

