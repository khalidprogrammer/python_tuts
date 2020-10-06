
# n! = n * n-1!

def factorial_iterative(n):
    fac=1
    for i in range(n):
        fac = fac * (i+1)
    return fac

def factorial_recursive(n):

    if n==1:
        return 1
    else:
        return n * factorial_recursive(n-1)

def fabonacii(n):

    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fabonacii(n-1) + fabonacii(n-2)

n = int(input("Enter Number \n"))
value = int(input("If you want Iterative apporch press 1 or Recursive apporoch press 2  and if  you want fabonacci press 3\n"))

if value == 1:
    print("Factorial iterative apporach",factorial_recursive(n))
elif value == 2:
    print("Factorial Recursive Apporach",factorial_recursive(n))
elif value ==3:
    print("Fabonacci series:", fabonacii(n))
else:
    print("Enter Valid numbers")



