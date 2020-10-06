
print("Enter Number ")
num = int(input())
num1 = 1
print("Enter Boolean Var 1 or 0 ")
var = int(input())
varbol = bool(var)
if varbol == True:
	while(True):
		print(num1 * "*")
		num1 = num1 + 1
		if num1 == num+1:
			break
else:
	while(True):
		print(num * "*")
		num = num - 1
		if num == num1-1:
			break