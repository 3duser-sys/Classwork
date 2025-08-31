import random
import time
playing = True
number = str(random.randint(0,9))

print("I will generate a number from 0 to 9, and you have to guess the number one digit at a time...")
time.sleep(0.01)
print("The game ends when you get the correct one.")
time.sleep(0.01)
print("Generating number fro 0 to 9")
time.sleep(1)
while playing:
    guess = input("Give it yor best shot :) \n")
    if number == guess:
        print("Haha You got it!")
        print("Your number was: ", number)
        time.sleep(0.01)
        print("GOOD JOB!")
    else:
        print("... Wasnt so correct, try again.")