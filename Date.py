class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    def display(self):
        return f"{self.year}/{self.month}/{self.day}"

    @classmethod
    def from_dash(cls,string):
          return cls(*string.split("-"))

date1=Date.from_dash("2008-12-5")
date2 =Date("2020","12","10")
print(date1.display())
print(date2.display())
#Output: 2008