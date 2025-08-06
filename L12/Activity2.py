lower = int(input("Tell me the lower number"))
upper = int(input("Tell me the higher number"))

print("prime numbrs between ",lower, "and", upper, "are:")

for num in range(lower,upper+1):
    if num>1:
        for i in range (2,num):
            if(num%i) == 0:
                break
        else:
            print(num)