class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class sportscar(Vehicle):
    pass

Lamborghini = sportscar("Lamborghini Urus", 305, 7.8)
print("Vehicle Name:", Lamborghini.name, "Speed", Lamborghini.max_speed, "km/h Mileage:", Lamborghini.mileage, "kmpl")