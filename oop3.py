# contructor is a magic method whenever we create
# object constructor method is called if you want
# some argument in Class so you can use constructor

class Employee:
    no_of_leaves = 8

    def __init__(self, name, salary, role):
        self.name = name
        self.__salary = salary
        self.role = role

    def printDetail(self):
        # text = "Hello World"
        # print(text.split())
        return f"Name is {self.name} and Salary is {self.__salary} and role is {self.role}"

    @classmethod
    def no_of_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split('-'))

    @classmethod
    def from_slash(cls, string):
        return cls(*string.split('/'))

    def set_salary(self,value):
        if value <=0:
            print("Your Salary is not negative or zero")
        else:
            self.__salary=value
    def get_salary(self):
        return self.__salary

harry = Employee("Khalid", 2500, "Insturctor")
rohan = Employee.from_dash("Rohan-200-student")
usman = Employee.from_slash("usman/300/student")


harry.set_salary(500)


print(harry.printDetail())

# print(rohan.printDetail())
# print(usman.printDetail())
# harry.no_of_leaves(34)
# Employee.no_of_leaves(45)
# print(Employee.no_of_leaves)
# print(harry.no_of_leaves)
