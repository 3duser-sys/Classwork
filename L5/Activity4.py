number = int(input("Enter Number to be INTERROGATED"))
print("Number to be questioned :", number)

if number %2==0:
    print("You are even so you are innocent", number, "You may leave.")

else:
    print("You are odd so you are guilty", number, "Send him to prison.")
