import datetime
import webbrowser
import pyttsx3

NAME = "Zara"
engine = pyttsx3.init()

def speak(text):
    print(f"{NAME}:", text)
    engine.say(text)
    engine.runAndWait()

speak(f"{NAME} online. How can I help?")

while True:
    command = input("You: ").lower()

    if "time" in command:
        speak(datetime.datetime.now().strftime("It is %I:%M %p"))
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")
    elif "exit" in command:
        speak("Goodbye")
        break
    else:
        speak("I don't know that command yet.")
