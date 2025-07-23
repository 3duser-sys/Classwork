print("ENTER A NUMBER (NUMERATOR)")
numn = int(input())
print("Enter a Number (Denominator) ")
numd = int(input())

if numn%numd == 0:
    print("\n" +str(numn)+ "is divisible by" +str(numd))
    print("= ", numn / numd)
else:
    print("\n" +str(numn)+ "is not divisible by" +str(numd))   