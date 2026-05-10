import requests


def get_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    

    if response.status_code == 200:
        print(f"IGNORE: Full JSON response: {response.json()}")
        joke_data = response.json()
        return f"{joke_data['setup']} - {joke_data['punchline']}"
    else:
        return "Failed to recieve joke."
    
def main():
    print("Welcome to the Rando-Joke GEN!!!")

    while True:
        user_input = input("PRES ENTER TO LAUGH, or q to be a party pooper.").strip()
        if user_input in ("q", "exit"):
            print("Ya just a party pooper, way to ruin the fun dude. Goodbye...")
            break
        
        joke = get_random_joke()
        print(joke)



if __name__ == "__main__":
    main()
