import random

class Fruit:
    def __init__(self):

        self.fruits = {
            "apple" : "red",
            "banana": "yellow",
            "grape": "purple",
            "orange": "orange",
            "kiwi": "green",
        }

    def start(self):
        print("The FRUIT QUIZ!!!!! **IMPORTANT**(USE ONLY LOWERCASE)")
        while True:
            fruit, color = random.choice(list(self.fruits.items()))
            colord = input("What is the color of {}?".format(fruit)).lower()

            if colord == color:
                print("COrrect!")
            else:
                print("Wrong!")
            option = int(input("0 to play again, if not 1."))
quiz = Fruit()
quiz.start()