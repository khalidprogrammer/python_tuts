import  switch
age = int(input("Enter your are age\n"))
#
# if int(age) == 18:
#     print("You are teen age")
# elif int(age) == 24:
#     print("You are the young")
#
# elif int(age) == 30:
#     print("You are mature")
#
# else:
#     print("invalid age")
if age < 18:
    print("You cannot drive")
elif age == 18:
    print("we will decide you can drive or nor")
elif age >60:

    print("Illegal age")

else:
    print("You are eligable")




