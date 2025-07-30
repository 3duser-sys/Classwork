"""Loops, Types of Loops, And For Loops
FOR, WHILE, NESTED"""

n = int(input("Enter the Number whose product you want to find"))
product = 1
for i in range(1, n*1):
    product = product*i
    print("\nproduct = ", product)