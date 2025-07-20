print("Enter Subjects")
markONE = int(input())
markTWO = int(input())
markTHREE = int(input())
markFOUR = int(input())
markFIVE = int(input())

tot = markONE+markTWO+markTHREE+markFOUR+markFIVE

avg = tot/5


if avg>91 and avg<=100:
    print("Your Grade is A+")
elif avg>=81 and avg<91:
    print("Your gRade is A")
elif avg>=71 and avg<81:
    print("Your gRade is B+")
elif avg>=61 and avg<71:
    print("Your gRade is B")
elif avg>=51 and avg<61:
    print("Your gRade is C+")
elif avg>=41 and avg<51:
    print("Your gRade is C")
elif avg>=31 and avg<41:
    print("Your gRade is D+")
elif avg>=21 and avg<31:
    print("Your gRade is D")
elif avg>=11 and avg<21:
    print("Your gRade is F")
elif avg>=0 and avg<11:
    print("Your gRade is F")
else:
    print("Dude I cant comprehend you")







