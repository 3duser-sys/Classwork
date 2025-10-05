class Person:

    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number
    
    def display(self):
        print("Name:", self.name)
        print("ID:", self.id_number)

class Employee(Person):

    def __init__(self, name, id_number, salary, post):
        self.salary = salary
        self.post = post

        Person.__init__(self, name, id_number)

Alex = Employee('Alex', 12345678, 1000000000, "Sales")

Alex.display()


