class Hedgehog:
    species = "american pygmy"

    def __init__(self, name, age):
        self.name = name
        self.age = age

Sonic = Hedgehog("Sonic",15)
Shadow = Hedgehog("Shadow",15)

print(Sonic.name,"age =", Sonic.age, )
print(Shadow.name,"age =", Shadow.age, )
