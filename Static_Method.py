
#  Static Method is type of method this method can access with class of instance or direct from Class
class Calculator:


    @staticmethod
    def add(num1,num2):
        return num1+num2




cal = Calculator()

print(Calculator.add(2,3))


