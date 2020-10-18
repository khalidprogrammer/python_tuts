class Computer:
    def __init__(self):
        self.__maxprice =900

    def sell(self):
        print(f"Your selling price is {self.__maxprice}")

    def setMaxPrice(self,price):

        if price <=0:
            print("Your price is not negative or zero")
        else:
            self.__maxprice = price

c = Computer()

c.setMaxPrice(1000)
c.sell()