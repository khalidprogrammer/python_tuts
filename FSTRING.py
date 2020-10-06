firstname = "Khalid"
lastname ="Usman"

#  Method 1 for string format
# fullname = "My name is %s %s" %(firstname,lastname)
# print(fullname)

# # Method 2 for string form
# fullname = "My name is {1} {0}"
# a = fullname.format(firstname,lastname)
# print(a)

#  Method f String for string format

fullname = f" my name is {firstname} {lastname} ages is {23} address is : {'kabul'} and our contact is 070202010"
print(fullname)