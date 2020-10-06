m = int(input("Enter the amount of medicine\n"))

d = int(input("Enter the percent amount \n"))

def Discountfn(m, d):
    discount = (d / 100) * m
    showfinal = m - discount
    return showfinal


print(Discountfn(m, d))
