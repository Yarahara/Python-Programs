__author__="Divine Gbagi"
__date__="11/04/2020"
"""This program creates a class for account with the attributes
    bank, type, and balance in a list
"""

class Account:
    __nextAcctID = 1000

    def __init__(self, tmpBank, tmpType, tmpBal):
        acctID = Account.__nextAcctID
        self.__listAcctInfo = [acctID, tmpBank, tmpType, tmpBal]
        Account.__setAcctID()

    def getAcctID(self):
        return self.__listAcctInfo[0] 
    
    def getBank(self):
        return self.__listAcctInfo[1]

    def setBank(self, newBank):
        self.__listAcctInfo[1] = newBank

    def getType(self):
        return self.__listAcctInfo[2]

##    def setType(self, newType):
##        self.__listAcctInfo[2] = newType

    def getBalance(self):
        return self.__listAcctInfo[3]

    def setBalance(self, newBal):
        self.__listAcctInfo[3] = newBal

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
        tmp += "Balance: " + "$" +str(self.getBalance()) + "\n"
        return tmp


        
        
