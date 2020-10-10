class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def GetArea(self):
        area = self.length * self.width
        return f"Area is {area}"


a = int(input("Enter length \n"))
b = int(input("Enter width \n"))
r1 = Rectangle(a, b)

# r1.length = int(input("Enter the lenght \n"))
# r1.width = int(input("Enter the width"))
print(r1.GetArea())
