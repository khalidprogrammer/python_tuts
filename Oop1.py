
class Employee:
    no_leaves =10
    average_age =20
    pass

harry = Employee()
rohan= Employee()


harry.name = "Harry"
harry.salary =40200
harry.role = "Software Developer"
harry.average_age =21
print(harry.__dict__)
print(Employee.average_age)
rohan.name = "rohan"
rohan.salary = 50000
rohan.role = "instructor"
rohan.no_leaves=12
print(rohan.__dict__)
print(Employee.no_leaves)
print(Employee.no_leaves)

