
# rows = int(input("Enter numbers of rows \n"))
# value = int(input("Press 1 for true and 0 for false"))
# if value ==1:
#     for i in range(0,rows+1):
#         print('*' * i)
# if value == 0:
#     for i in range(rows,0,-1):
#         print("*" * i)

rows = int(input("Enter number of rows \n"))
if rows < 1:
    print("invalid input")
value = int(input("Enter 1 for True and 0 for False \n"))

def starpattern(rows,value):
    try:
        if value == 1:
            i = 1
            while i <= rows:
                print("*" * i)
                i = i + 1
        elif value == 0:
            while rows > 0:
                print("*" * rows)
                rows = rows - 1
        else:
            print("invalid")
    except Exception as e:
        print(e)



starpattern(rows,value)
