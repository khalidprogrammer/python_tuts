from pygame import mixer
import calendar

print("========================Welcome to Play audio===============================\n ")
enter_name = input("Please Enter Your Name \n")
m = int(input("Enter month \n"))
y = int(input("Enter year \n"))
mycalender = calendar.month(y, m)

print(mycalender)


def playsound(file, stopper):
    # initialize mixer function
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input("Enter 'stop' to the stop water alram\n")
        if a == stopper:
            mixer.music.stop()
            break


if __name__ == '__main__':
    playsound('water.mp3', 'stop')
