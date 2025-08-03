num1 = float(input("Enter value 1"))

num2 = float(input("Enter value 2"))

while(num2!= 0):
    temp = num2
    num2 = num1 % num2
    num1 = temp

hcf = num1

print("HCF of the two numbers is",hcf)