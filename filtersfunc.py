# list_1 =["khalid","walid","imran","ikram"]
#
# def identify_name(name):
#    return name.endswith('n')
#
# identi=list(filter(identify_name,list_1))
# print(identi)

# dicName ={1:"Khalid",2:"Usman",3:"imran",4:"sam",5:"Ali" }
# newDict=dict()
#
# for key,value in dicName.items():
#     if key % 2==0:
#         newDict[key]=value
# print(newDict)

# l1 = [18,19,20,22,32,31,32]
#
# def candrink(ages):
#     return ages >20
#
# canDrink=list(filter(candrink,l1))
# print(canDrink)

companies= [{"name": "Company One", "category": "Finance", "start": 1981, "end": 2003},
  {"name": "Company Two", "category": "Retail", "start": 1992, "end": 2008},
  {"name": "Company Three", "category": "Auto", "start": 1999, "end": 2007},
  {"name": "Company Four", "category": "Retail", "start": 1989, "end": 2010},
  {"name": "Company Five", "category": "Technology", "start": 2009, "end": 2014},
  {"name": "Company Six", "category": "Finance", "start": 1987, "end": 2010},
  {"name": "Company Seven", "category": "Auto", "start": 1986, "end": 1996},
  {"name": "Company Eight", "category": "Technology", "start": 2011, "end": 2016},
  {"name": "Company Nine", "category": "Retail", "start": 1981, "end": 1989}
]
def show():
    for value in companies:
        if value['category'] == 'Auto':
            print(value)

show()
