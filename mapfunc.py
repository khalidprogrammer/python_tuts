# numbers =["34","5","33","60"]
# num_list =[]
# numbers =list(map(int,numbers))
#
#  for i in range(len(numbers)):
#      numbers[i]= int(numbers[i])
#
# numbers[2] =numbers[2]+2
# print(numbers[2].append(num_list))

num = [1,2,4,5,44,11]

# numbers=list(map(lambda x:x*x,num))
# print(numbers)
def square(a):
    return a*a
def cube(a):
    return a*a*a
func =[square,cube]
print('====================list with square and cuber======================\n')
for i in range(len(num)):
    val = list(map(lambda x:x(i),func))
    print(val)


print(f"list without===================\n {num}")