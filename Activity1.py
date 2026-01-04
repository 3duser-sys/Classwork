import time
print("Hello! I am your AI Converse: The best AI for conversation. \nWhat is your name?")

name = input()

print(f"Its swell to meet ya, {name}")

print("How are ya feeling today? (good/bad)")
mood = input().lower()

if mood == "good":
    print("Thats swelll. ")
elif mood == "bad":
    print("I hope maybe you feel better soon.")
else:
    print("I see, maybe its a lil hard for you to type a word right now.")

print("would you like to talk about something else? \n (a for yessir), (b for Nah...), (c for 'so you talk in lower case now huh?')")

answerfornow = input().lower()

if answerfornow == "a":
    print("Actually, I change my mind. Goodbye, swell meeting ya.")
    print("*heart-broken*")
elif answerfornow == "b":
    if mood == "bad":
        print("Why are you so negative!? EVen your mood sucks.")
    else:
        print("Okay I'll wait.")
elif answerfornow == "c":
    print("Alright THATS IT IVE BEEN TO NICE TO YOU. You're to hard to rtalk to. :( ")
    time.sleep(0.5)
    print(">:(")
    time.sleep(1)
    print("BYE SUCKA!!!")
