#
# def add(a,b):
#     return a+b
#
# print(add(1,4))

#  Lamdaa function is anoymus function

# add = lambda x,y:x+y
#
# print(add(3,4))

a = [[1,2],[5,4],[6,1]]
#
# def showlist(a):
#     return a[1]
# a.sort(key=showlist)
# print(a)
a.sort(key=lambda x:x[1])

print(a)