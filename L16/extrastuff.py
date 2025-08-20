print("Addition and Subtraction")

def add(X,Y):
    return X+Y

def subt(X,Y):
    return X-Y

while True:
    add_subt = input("Would you like to ADD(Y) or SUBTRACT(N)?:  ")
    enter1 = int(input("What is number 1?"))
    enter2 = int(input("What is number 2?"))

    if add_subt == "Y":
        print(enter1,"+",enter2,"=",add(enter1,enter2))
    elif add_subt == "N":
        print(enter1,"-",enter2,"=",subt(enter1,enter2))

    print("Thanks for using")