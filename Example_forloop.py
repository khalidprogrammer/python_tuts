# # Example in list
#
# list_number = [2,32,2,21,2]
# dic_student =[{'name':"Khalid",'address':'peshawar'},{'name':'usman','address':'kabul','contact':'030202021'}]
#
# type = input("Enter type of data\n")
#
# if type == 'list':
#     for item in list_number:
#         print(item)
# elif type == 'dict':
#     for item in dic_student:
#         print(item['name'])
# else:
#     print('invalid type')

# # range function
# print(range(10))
#
# print(list(range(10)))
#
# print(list(range(2, 8)))
# first agrument use for start and second for stop and third to add 3
# print(list(range(2, 10, 3)))

#  program to display student's marks from record

student_name = 'khalid'

# marks = {'James': 90, 'Jules': 55, 'Arthur': 77}
#
# for student in marks:
#     if student == student_name:
#         print(f"{student_name} is : {marks[student]}")
#         break
# else:
#     print('No entry with that name found.')
#
#
#  Example of break  statment for
# for i in range(0,10):
#     if i == 3:
#         break
#     print(i)

# i = 0
# while i <=10:
#
#     if i == 3:
#         break
#     print(i)
#     i= i+1
# create a program  so that all item can printed expected swift and c++
# list_program =['python','java',"Swift","C","C++"]
#
# for program in list_program:
#     if program =="Swift" or program =='C++':
#         continue
#     print(program)

#  Print table

# number=int(input('Enter Integer \n'))
#
# for count in range(1,11):
#     product = number * count
#     print(f" {number} x {count}={product}")

number= int(input("Enter an Integer :"))
i=10
while i >= 1:
    product =number * i

    i = i - 1
    print(f"{number} x {i} = {product}")

#write a program to find the sume of the numbers from 1 to 100

# total =0
# for num in range(1,101):
#      total= total + num
#
# print(total)













