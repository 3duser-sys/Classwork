try:
    number = int(input("Enter a number: "))
    print("Your number is: ", number)
except ValueError as error:
    print("Exception:", error)