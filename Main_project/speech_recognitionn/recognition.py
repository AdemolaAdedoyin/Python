import speech_recognition as sr
from pprint import pprint
# TO RECOGNIZE THE AUDIO
recognize = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something")
    audio = recognize.listen(source)

try:
    print("You said " + recognize.recognize_google(audio))
    val = recognize.recognize_google(audio)
    # pprint("You said " + recognize.recognize_google(audio, show_all=True))
    if val == "what is your name":
        print("I am Alexa")
    elif val == "Who are you".lower():
        print("I am me")
except sr.UnknownValueError:
    print("Did not understand")
except sr.RequestError:
    print("Could not request results")


# # TO SAVE THE AUDIO TO AN AUDIO FILE
# with open("microphone-results23.aiff", "wb") as f:
#     f.write(audio.get_aiff_data())