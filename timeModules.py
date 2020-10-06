import time
initial = time.time()
k=0
while(k<45):
    print("While loope")
    # time.sleep(2)
    k+=1
print("time is :", time.time() - initial,"Seconds")

inital2= time.time()
for i in  range(30):
    print("for loop")

print("time is:",time.time()-inital2,"sec")

localtime = time.asctime(time.localtime())
print(localtime)