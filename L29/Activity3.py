class Bird:

    def __init__(self):
        print("Bird is amazing!")

    def whoIam(self):
        print("Bird")

    def fly(self):
        print("Just fly!")

class Penguin(Bird):

    def __init__(self):
        super().__init__()
        print("Penguin is better!")
    def whoIam(self):

        print("Penguin!")
    def swim(self):

        print("But I cant. I can only swim! (RAGER (:)")

swoosh = Penguin()
swoosh.whoIam()
swoosh.fly()
swoosh.swim()