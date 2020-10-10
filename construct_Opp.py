# contructor is a magic method whenever we create
# object constructor method is called if you want
# some argument in Class so you can use constructor

class Employee:
    no_of_leaves= 8
    def __init__(self,name,salary,role):
        self.name =name
        self.salary=salary
        self.role=role


    def printDetail(self):
        text= "Hello World"
        print(text.split())
        return f"Name is {self.name} and Salary is {self.salary} and role is {self.role}"
    @classmethod
    def no_of_leaves(cls,newleaves):
        print(cls)
        cls.no_of_leaves = newleaves
    


harry = Employee("Khalid",2500,"Insturctor")

print(harry.salary)

print(harry.printDetail())

# harry.no_of_leaves(34)
Employee.no_of_leaves(45)
print(Employee.no_of_leaves)
print(harry.no_of_leaves)