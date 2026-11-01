import asyncio
import speech_recognition as sr
import pyttsx3
from googletrans import Translator

def speak(text, language="en"):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    voices = engine.getProperty("voices")

    if language == "en":
        engine.setProperty("voice", voices[0].id)

    else:
        engine.setProperty("voice", voices[1].id)

    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please now speak en ingles...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing :3")
        text = recognizer.recognize_google(audio, language="en-US")
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"TIS AN API ERRORRR >: {e}")\
    
    return ""

def translate_text(text, target_language="es"):
    translator = Translator()
    translation = asyncio.run(translator.translate(text, dest=target_language))
    print(f" Translated text: {translation.text}")
    return translation.text
        
def display_language_options():
    print("???? Available translation languages: ")
    print("1. Hindi (hi)")
    print("2. Tamil (ta)")
    print("3. Telugu (te)")
    print("4. Bengali (bn)")
    print("5. Marathi (mr)")
    print("6. Gujarati (gu)")
    print("7. Malayalam (ml)")
    print("8. Punjabi (pa)")
    print("9. Kannada (kn)")
    print("10. Odia (or)")
    print("11. French (fr)")
    print("12. German (de)")
    print("13. Italian (it)")
    print("14. Japanese (ja)")
    print("15. Korean (ko)")
    print("16. Portuguese (pt)")
    print("17. Russian (ru)")
    print("18. Spanish (es)")
    print("19. Turkish (tr)")

    choice = input("Enter the number corresponding to your choice: ")
    language_dict = {
        "1": "hi",
        "2": "ta",
        "3": "te",
        "4": "bn",
        "5": "mr",
        "6": "gu",
        "7": "ml",
        "8": "pa",
        "9": "kn",
        "10": "or",
        "11": "fr",
        "12": "de",
        "13": "it",
        "14": "ja",
        "15": "ko",
        "16": "pt",
        "17": "ru",
        "18": "es",
        "19": "tr"
    }
    return language_dict.get(choice, "es")


def main():
    target_language = display_language_options()
    original_text = speech_to_text()
    if original_text:
        translated_text = translate_text(original_text, target_language=target_language)
        speak(translated_text, language="en")
        print(f"Transltion has been spoken!")


if __name__ == "__main__":
    main()