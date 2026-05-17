import requests
import random
import html

edu_catg = 9
API_URL = f"https://opentdb.com/api.php?amount=10&category={edu_catg}&type=multiple"
def get_edu_questions():
    response = requests.get(API_URL)
    

    if response.status_code == 200:
        data = response.json()
        if data['response_code'] == 0 and data['results']:
            return data['results']
    
    return None

def run_quiz():

    questions = get_edu_questions()

    if not questions:
        print('Failed to Fetch')
        return
    
    score=0
    print("Educational quiz is a go! (Time to sufferrrrr)\n")

    for i, q in enumerate(questions, 1):
        questions = html.unescape(q['question'])
        correct = html.unescape(q['correct_answer'])
        incorrects = [html.unescape(a) for a in q['incorrect_answers']]

        options = incorrects + [correct]
        random.shuffle(options)

        print(f"Question {i}: {questions}")
        for idx, option in enumerate(options, 1):
            print(f"   {idx}. {option}")

        while True:

            try:
                choice = int(input("\nYour answer (1-4):"))

                if 1 <= choice <= 4:
                    break

            except ValueError:
                pass
            print("Invalid input! Enter 1-4 dingus!! smart enough to do that??")

        if options[choice-1] ==  correct:
            print("✅🏁 That is correct! Man, your'e smart! I don't want to be the computer anymore :(\n")
            score =+1
        else:
            print(f"😆😆😆HA😆😆😆 WRONG!! Correct Answer: {correct}\n (i know u can do better)\n")

    print(f"Final Score: {score}/{len(questions)}")
    print(f"Percentage: {score/len(questions)*100:.1f}%")

if __name__ == "__main__":
    run_quiz()