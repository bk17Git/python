import speech_recognition

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Say something: ")
    audio = recognizer.listen(source)

words = recognizer.recognize_google(audio)

if "hello" in words:
    print("Hello to you too!")
elif "how are you" in words:
    print("I am fine.Thank you!")
elif "goodbye" in words:
    print("Goodbye!!!")
else:
    print("Huh!")