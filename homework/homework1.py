import time
import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()

history = []
positive_count = 0
negative_count = 0
neutral_count = 0

def show_processing_animation():
    print(Fore.CYAN + "🕵️ Analyzing", end="")
    for _ in range(3):
        time.sleep(0.4)
        print(".", end="")
    print(Style.RESET_ALL)

def analyze_sentiment(text):
    global positive_count, negative_count, neutral_count
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.25:
        positive_count += 1
        return "Positive", polarity
    elif polarity < -0.25:
        negative_count += 1
        return "Negative", polarity
    else:
        neutral_count += 1
        return "Neutral", polarity

def execute_command(command):
    global history, positive_count, negative_count, neutral_count

    if command == "help":
        print(Fore.YELLOW + "Commands: help | history | summary | reset | exit" + Style.RESET_ALL)

    elif command == "history":
        if not history:
            print(Fore.YELLOW + "No history yet." + Style.RESET_ALL)
        else:
            for i, item in enumerate(history, 1):
                print(f"{i}. {item}")

    elif command == "summary":
        print(Fore.CYAN + "Mission Summary" + Style.RESET_ALL)
        print(Fore.GREEN + f"Positive: {positive_count}" + Style.RESET_ALL)
        print(Fore.RED + f"Negative: {negative_count}" + Style.RESET_ALL)
        print(Fore.YELLOW + f"Neutral: {neutral_count}" + Style.RESET_ALL)

    elif command == "reset":
        history.clear()
        positive_count = 0
        negative_count = 0
        neutral_count = 0
        print(Fore.CYAN + "All data reset." + Style.RESET_ALL)

def get_valid_name():
    while True:
        name = input(Fore.MAGENTA + "Enter your name: " + Style.RESET_ALL).strip()
        if name.isalpha():
            return name
        print(Fore.RED + "Name must contain only letters." + Style.RESET_ALL)

print(Fore.CYAN + "👋 Welcome to Sentiment Spy!" + Style.RESET_ALL)

username = get_valid_name()

print(Fore.CYAN + f"Hello, Agent {username}!" + Style.RESET_ALL)
print(Fore.YELLOW + "Type text or a command. Type help for commands." + Style.RESET_ALL)

while True:
    user_input = input(Fore.GREEN + ">> " + Style.RESET_ALL).strip()

    if user_input == "":
        print(Fore.RED + "Please enter text." + Style.RESET_ALL)
        continue

    if user_input.lower() == "exit":
        break

    if user_input.lower() in ["help", "history", "summary", "reset"]:
        execute_command(user_input.lower())
        continue

    show_processing_animation()
    sentiment, polarity = analyze_sentiment(user_input)
    history.append((user_input, sentiment, round(polarity, 2)))

    if sentiment == "Positive":
        print(Fore.GREEN + f"😊 Positive ({polarity:.2f})" + Style.RESET_ALL)
    elif sentiment == "Negative":
        print(Fore.RED + f"😔 Negative ({polarity:.2f})" + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + f"😐 Neutral ({polarity:.2f})" + Style.RESET_ALL)

print(Fore.CYAN + "Final Mission Report" + Style.RESET_ALL)
print(Fore.GREEN + f"Positive: {positive_count}" + Style.RESET_ALL)
print(Fore.RED + f"Negative: {negative_count}" + Style.RESET_ALL)
print(Fore.YELLOW + f"Neutral: {neutral_count}" + Style.RESET_ALL)

filename = f"{username}_sentiment_analysis.txt"
with open(filename, "w") as file:
    file.write("Sentiment Spy Mission Report\n")
    file.write(f"Agent: {username}\n\n")
    file.write(f"Positive: {positive_count}\n")
    file.write(f"Negative: {negative_count}\n")
    file.write(f"Neutral: {neutral_count}\n\n")
    for item in history:
        file.write(str(item) + "\n")

print(Fore.CYAN + f"Report saved to {filename}" + Style.RESET_ALL)
print(Fore.BLUE + "👋 Mission complete. Goodbye!" + Style.RESET_ALL)
