print("============================ Welcome  To Faulty Calculator=========================")
print("================Please enter this operator +,*,/,_,%** =================================")


def calculator():
    operator = input("Enter operator\n")
    number1 = int(input("Enter num1 \n"))
    number2 = int(input("Enter num2 \n"))
    if operator == '+':
        if number1 == 56 and number2 == 9:
            print("77")
        else:
            print("sum is", number1 + number2)
    elif operator == '*':
        if number1 == 45 and number2 == 3:
            print("556")
        else:
            print("multiplication", number1 * number2)
    elif operator == '/':
        if number1 == 56 and number2 == 6:
            print("4")
        else:
            print("dividision:", float(number1) / float(number2))
    elif operator == '-':
        print("substraction :", number1 - number2)
    elif operator == "%":
        print("Module is :", number1 % number2)
    elif operator == "**":
        print("power is", number1 ** number2)

    else:
        print("Unexpect error ! please enter valid number and operator")
    again()


def again():
    cal_again = input(''' Do you want continoue the calculation please type Y and want To exit type N \n ''')
    if (cal_again == 'Y'):
        calculator()
    elif (cal_again == 'N'):
        print("calculator is exit")
    else:
        again()


calculator()
