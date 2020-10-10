

i =2
while i <=60:
    j=2
    # b= True
    while j <= i-1:

        if i%j == 0:
            # b= False
            break
        j = j + 1
    if i== j:
        print("Prime number is:",i)
    i=i+1