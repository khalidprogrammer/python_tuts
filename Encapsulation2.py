
class Account:
    __account_num= 1000
    __acount_balance =200

    @staticmethod
    def setValues( __account_balance):
        if __account_balance <=0:
            print("Invalid input")
        else:
           account  =__account_balance +1
    @staticmethod
    def getDesposit(__account_balance):
        print(f"Your account balance is {__account_balance}")

class Hackers:
    acc = Account()
    acc.__account_balance =100
    acc.setValues(100)
    acc.getDesposit()




