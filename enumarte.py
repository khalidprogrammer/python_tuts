list = ['book', 'computer', 'mobile', 'usb', 'hardrive', 'keyboard']
#
# # i=1
# # for item in list:
# #     if i%2 is  0:
# #         print(f"item is {item}")
# #     i+=1
#
for count,item in enumerate(list,start=1):
    if count % 2 is not 0:
        print(item)
#
# grocery =['bread','milk','butter']
#
# enumerategrocery =enumerate(grocery)
# print(type(enumerategrocery))
#
# print(list(enumerategrocery))
#
# enumerategrocery =enumerate(grocery,100)
#
# print(list(enumerategrocery))