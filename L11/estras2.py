number = int(input("Number please"))
wouldulike = input("DO you want to add up even numbers/ odd numbers (even/odd)")
if wouldulike == "even":
    while number != 0:
        number = number-1
        if number % 2 == 0:
            print(number)

elif wouldulike == "odd":
    while number != 0:
        number = number-1
        if number % 2 != 0:
            print(number)

else:
    print("I AM JUST A ROBOT I CANT DO EVERYTHING")