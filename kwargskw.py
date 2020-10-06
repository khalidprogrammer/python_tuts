# if you wanaa to pass multiple argument so you can use kwargs and *agrs


# def funargs(normal,*args, **a):
#     print(normal)
#     for item in args:
#         print(item)
#     for key,value in a.items():
#         print(f"{key}  {value}")
#
# normal ="Hello this normal argumet"
#
# har = ["Khalid","Usman","Imran"]
# kw = {"Khalid":"Eating Meal","Naveed":"Eating chocklate","imran": "Eating pizza","salman":"cook"}
#
# funargs(normal,*har,**kw)

def fullname(**kids):
    print(f"fullname is {kids['fname']} {kids['lname']}")

fullname(fname="Khalid",lname ="Usman")