class Employee:
    def __init__(self,name,address,skill,salary):
        self.name = name
        self.address= address
        self.skill =skill
        self.salary = salary

    def PrintDetail(self):

        return f"Name is {self.name} \n and Address {self.address} \n skill is {self.skill} \n Salary is {self.salary}  "


e1 = Employee("Khalid","Peshawar","Web Developer","5000")

print(e1.PrintDetail())


class CoolProgramer (Employee):
    no_holiday =50
    def __init__(self, name, address, skill, salary,language):
        super(Employee, self).__init__(Employee.name,Employee.address,Employee.skill,Employee.salary)
        self.languge =language
    def printCoolProg(self):
        return f"Name is {self.name} \n and Address {self.address} \n skill is {self.skill} \n Salary is {self.salary} \n language is {self.language} "
    def getlang(self):
        for item in self.language:
            print(item)


usman = CoolProgramer("usman","Peshawar","Instructor","600",["c++","C","Python"])

print(usman.printCoolProg())
usman.getlang()
print(usman.no_holiday)


