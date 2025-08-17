print("Python calculator! Max digits are two.")
def addition(num1,num2):
    return num1 + num2
def subtraction(num1,num2):
    return num1 - num2
def multiplication(num1,num2):
    return num1 * num2
def division(num1,num2):
    return num1 / num2

print("Please select the operation,")
print("a. Add")
print("b. subtract")
print("c. multiply")
print("d. divide")

choice = input("Please ebter a/b/c/d.")

num1 = int(input("Please enter number 1:"))
num2 = int(input("Please enter number 2:"))

if choice == "a":
    print(num1, "+", num2, " = ", addition(num1,num2))
    
elif choice == "b":
    print(num1, "-", num2, " = ", subtraction(num1,num2))
elif choice == "c":
    print(num1, "*", num2, " = ", multiplication(num1,num2))
elif choice == "d":
    print(num1, "/", num2, " = ", division(num1,num2))

