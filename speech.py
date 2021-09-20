import pyttsx3

engine = pyttsx3.init()

name = input("What is your name: ")
gender = input("Write M for Male and F for Female: ")

if gender.lower() == "m":
    engine.say(f"Hello Mr.{name}")
elif gender.lower() == "f":
    engine.say(f"Hello Miss{name}")
else:
    engine.say("Please choose you gender correctly!")

engine.runAndWait()
