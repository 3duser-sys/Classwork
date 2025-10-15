import time
class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word+ ' ( '+self.meaning+ ')'

flash = []

print("The Falashcardo:")
print("Get Started:")

while True:
    word = input("Enter the term you would like to define: ")

    meaning = input("Enter the meaning of the term: ")

    flash.append(flashcard(word, meaning))
    option = int(input("enter 0 if you woud like to continue, 1 if you want to quit"))

    if (option):
        break

print("\nDoing the Hard work...")
time.sleep(2)

print("\n\n Your flashcards,")

for i in flash:
    print(">", i)