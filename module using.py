import random
import math
import platform


x = platform.system()
print(x)

rand_number = random.randint(1,6)

rand=random.random()*100

lst =["Book_title","Book_author","Book_publisher","Book_desciption","Book_year"]

rand_lst = random.choice(lst)

print(rand_lst)

num = int(input("Enter the square root \n"))

square_root = math.sqrt(num)

print(square_root)