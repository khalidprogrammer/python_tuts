from pygame import mixer
from datetime import datetime
from time import time

print("=====================================Welcome Healthy Programmer App=======================\n")


def playsound(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break


def log_now(msg):
    with open('my_log.txt', 'a') as f:
        f.write(f" {msg} {datetime.now()}\n")


if __name__ == '__main__':
    #  Initilazation time
    water_time = time()
    # eyes_time = time()
    excercise_time = time()
    #  time in seconds
    water_secs = 10
    # eyes_secs = 40*60
    excercise_secs = 10

    while True:
        if time() - water_time > water_secs:
            print("Now Water Drinking time Enter 'drank' to stop alarm\n ")
            playsound('water.mp3', 'drank')
            water_time = time()
            log_now("Drink Water at")
        if time() - excercise_time > excercise_secs:
            print("Now Its Excercise Time Enter 'donepy'\n")
            playsound('Excercise.mp3', 'donepy')
            excercise_time = time()
            log_now("Excercise  at")
