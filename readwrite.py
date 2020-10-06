# f = open("khalid1.txt","r+")
# print(f.read())
# f.write("thank you\n")
#
# f.close()

# f = open("khalid.txt")
#  read line function is used for read the file line by line
# tell() function is work where you line character is start
# print(f.tell())
# print(f.readline())
# print(f.tell())
# listOne = [20, 40, 60, 80]
# listTwo = [20, 40, 60, 80]
# print(listOne == listTwo)
# print(listOne is listTwo)
# print(f.readline())
# print(f.tell())
# print(f.readline())
# print(f.tell())
# print(f.seek(5))
# print(f.readline())

with open("khalid.txt") as f:
    print(f.readlines())


f = open("khalid.txt","rt")

f.close()

print(f.__doc__)


