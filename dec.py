# def func1():
#     print("Please find function")
#
# func2 = func1
#
# del func1
#
# func2()
# return function inside function
# def executor(num):
#     if num == 0:
#         return max
#     if num ==1:
#         return float
#
# print(executor(0))

#  Now we can pass function as parameter

#  Now Decorator can modify the function functionality


def funcparam(funct1,funct2):
    def add ():
        funct1()
        print(f"sum is {5+6}")
        print(f"minus:{6-3}")
        funct2(3)
    return add



def power_func(a):
    return a*a

def who_is_khalid():
    print("Khalid is a good boy")

who_is_khalid = funcparam(who_is_khalid,power_func)
print(who_is_khalid)





