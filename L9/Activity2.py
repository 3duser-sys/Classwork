units = int(input("Your amount of units:"))

if (units<50) :
    print(2.60 * units)
    print("tax is 25")
    amount = 2.60 * units+25

elif (units>50 and units<100) :
    print(3.25 * units)
    print("tax is 35")
    amount = 3.25 * units + 35

elif (units>100 and units<200) :
    print(5.26 * units)
    print("tax is 45")
    amount = 5.26 * units + 45

elif (units<=200):
    amount = 130 + 162.50 + ((units - 100)* 5.26)
    surcharge = 45
else:
    amount = 130 + 162.50 + 526 + ((units - 200) * 8.45)
    surcharge = 75

print(amount)