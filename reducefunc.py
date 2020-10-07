from functools import reduce
list1 = [1,2,3,4,2]
#
# sum_list= reduce(lambda x,y:x+y,list1)
# print(sum_list)

# num =0
# for item in list1:
#     num=num+item
#
# print(num)
def add(a,b):
    return a+b
total_sum = reduce(add,list1)
print(total_sum)