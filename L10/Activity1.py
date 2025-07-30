"""Loops, Types of Loops, And For Loops
FOR, WHILE, NESTED"""

n = int(input("Enter the Number whose sum you want to find"))
sum = 0
for i in range(1, n+1):
    sum = sum+i
    print("\nSum = ", sum)