# # i = 0
# # while (i < 45):
# #     print(i)
# #     i= i+1
# list1 = ["khalid","usman"]
#
# i=0
#
# while(True):
#     print(len(list1))
#     i = i+1
#


#
# while(True):
#     i = int(input("Enter number"))
#     if i+1 < 100
#         i= i+1
#         print(i)
#         continue
#     if i > 100:
#         break
#         i=i+1


# Guess game
def guessgame():
    no_guess = 1

    while (no_guess <= 5):
        guess = int(input("Enter your guess number\n"))
        if guess < 20:
            print("Your number is smaller and guess no is greather")
        elif guess > 20:
            print("your number is grater and guess no is smaller")

        else:
            print("=======================You Won =============  \n")
            print(no_guess, "No of guess he took to finish")
            again()
            break
        print(5 - no_guess, "No of guess left")
        no_guess = no_guess + 1

        if (no_guess > 5):
            print("Game Over")


def again():
    cal_agin = input('''  If you want to continue game please press Y and if you exit to game please Enter N \n ''')
    if(cal_agin == 'Y'):
        guessgame()
    elif (cal_agin=='N'):
        print("You exit the game ")
    else:
        again()

guessgame()

