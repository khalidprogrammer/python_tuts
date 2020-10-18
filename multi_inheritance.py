class Employee:
    var =15
    def __init__(self,name,address,skill,salary):
        self.name = name
        self.address= address
        self.skill =skill
        self.salary = salary

    def PrintDetail(self):

        return f"Name is {self.name} \n and Address {self.address} \n skill is {self.skill} \n Salary is {self.salary}  "
    def printBase1(self):
        print("Base1")


class Player:

    def __init__(self,name,game):
        self.name =name
        self.game=game
    

    def getName(self):
        for item in self.game:
            print(item)

    def PrintPlayer(self):
        print(f" Name of the player is {self.name} and game is {self.game}")

    def Hello(self,string):
        return string



class CoolProgrammer(Player,Employee):
    langauge = "C++"

    def printLang(self):
        print(self.langauge)

islam = Player("islam",["hockey"])
khalid = CoolProgrammer("khalid",["game1","game2"])
print(khalid.Hello("Khlaid"))
khalid.printBase1()
print(khalid.var)