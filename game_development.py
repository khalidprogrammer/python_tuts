import random

list = ['s', 'w', 'g']

print('======================================SNAKE WATER GUN========================\n')
print("Please Enter with lowercase\n s=Snake\n w=Water\n g=Gun")
chance = 10
no_chance = 0
computer_point = 0
human_point = 0

while no_chance < chance:
    user_input = input("Enter s for Snake and w for Water and g for Gun \n")
    comp_num = random.choice(list)
    if user_input == comp_num:
        print(f"game is tie user guess {user_input} and computer guess {comp_num}")
    # Computer Game Won
    elif user_input == 's' and comp_num == 'g':
        computer_point = computer_point + 1
        print(f"computer guess {comp_num} and You guess {user_input}\n")
        print(f"computer won with 1 point \n")
        print(f"computer point is {computer_point} and Your point is {human_point}")
    elif user_input == 'w' and comp_num == 's':
        computer_point = computer_point + 1
        print(f"computer guess {comp_num} and You guess {user_input}\n")
        print(f"computer won with 1 point \n")
        print(f"computer point is {computer_point} and Your point is {human_point}")
    elif user_input == 'g' and comp_num == 'w':
        computer_point = computer_point + 1
        print(f"computer guess {comp_num} and You guess {user_input}\n")
        print(f"computer won with 1 point \n")
        print(f"computer point is {computer_point} and Your point is {human_point}")
    # End Computer Game
    # Start User Game
    elif user_input == 's' and comp_num == 'w':
        human_point = human_point + 1
        print(f"You guess {user_input} and computer guess {comp_num}\n")
        print(f"You won with 1 point \n")
        print(f"Your point is {human_point} and computer point is {computer_point}")
    elif user_input == 'g' and comp_num == 's':
        human_point = human_point + 1
        print(f"computer guess {comp_num} and You guess {user_input}\n")
        print(f"You won with 1 point \n")
        print(f"Your point is {human_point} and computer point is {computer_point}")
    elif user_input == 'w' and comp_num == 'g':
        human_point = human_point + 1
        print(f"You guess {user_input} and computer guess {comp_num}\n")
        print(f"You won with 1 point \n")
        print(f"Your point is : {human_point} and computer point is : {computer_point}")
    else:
        print("invalid Input")

    no_chance = no_chance + 1
    print(f"{chance - no_chance} is left chance out of: {chance}")

print("Game is over !!!!!!!!")

if computer_point > human_point:
    print(f"Computer won the game with point : {computer_point}")
else:
    print(f"Human won the game with point : {human_point}")
