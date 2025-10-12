from abc import ABC, abstractmethod

class Animal(ABC):

    def move(self):
        pass

class HUMANS(Animal):
    def move(self):
        print("I got two legs, not four")
        print("I can walk and run (Faster than you)")

class Snake(Animal):

    def move(self):
        print("Were the slithering snakes, seriously dangerous")
        print("As were gliding across the floor")

class Dog(Animal):

    def move(self):
        print("We are humans best friends, four legs and a sprint like a panther")

class Cat(Animal):
    
    def move(self):
        print("Burnt the dogs, although also 4 legs, built a place for me,")
        print("That sweet sweet place on that sweet sweet couch!")

class Hedgehog(Animal):

    def move(self):
        print("Usually slower than eveyone, somehow i survived. Also 4 legs but theres an exception")
        print("With that fast boy, Sonic the hedgehog.")

H = HUMANS()
H.move()


S = Snake()
S.move()


H = Dog()
H.move()


S = Cat()
S.move()


H = Hedgehog()
H.move()
