class test:
    def __init__(self,a):
        self.a = a
    
    def __lt__(self, other):
        if self.a < other.a:
            return "obj is less thn obj2"
        else:
            return "obj2 is less than obj"
    
    def __eq__(self, other):
        if self.a == other.a:
            return "They are equal"
        else:
            return "Not equal"

obj = test(2)
obj2 = test(3)

print("Passed Values: ", obj.a, obj2.a)
print(obj < obj2)


obj3 = test(5)
obj4 = test(5)

print("Passed Values: ", obj3.a, obj4.a)
print(obj3 == obj4)