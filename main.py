import speech_recognition as sr
import pyttsx3
from AppOpener import open, close

engine = pyttsx3.init()
instance = sr.Recognizer()


def get_voice():
    with sr.Microphone() as source:

        # adjustment = instance.adjust_for_ambient_noise
        instance.energy_threshold = 1000
        
        audioData = instance.listen(source)
        dataString = ""

        try:
            dataString = instance.recognize_google(audioData) 
            # print("You:", instance.recognize_google(audioData))
        except sr.UnknownValueError as error:
            print(f"{error}")
        except sr.RequestError:
            print("Request Error")

        return dataString
    

def get_respond(command):
    if "open" in command:
        openCommand = command.replace("open", "")
        # print(f"Opening{openCommand}")
        engine.say(f"Opening{openCommand}")
        engine.runAndWait()

        open(openCommand)

    if "close" in command:
        closeCommand = command.replace("close", "")
        # print(f"Closing{closeCommand}")
        engine.say(f"Closing{closeCommand}")
        engine.runAndWait()
        
        close(closeCommand)

def get_command(audio):

    if "open" in audio:
        openCommand = audio
        get_respond(openCommand)
        # print(f"Opening {openCommand}.")

    if "close" in audio:
        closeCommand = audio
        get_respond(closeCommand)

    if "exit" in audio:
        engine.say("Are you sure you want to close me?")
        engine.runAndWait()
        audio = get_voice()
        if "yes" in audio:
        # print("Just run me again when you need me.")
            engine.say("Just run me again when you need me.")
            engine.runAndWait()
            exit()
        else:
            engine.say("It's my pleasure to continue serving you.")
            engine.runAndWait()
            audio = get_voice()
            get_command(audio)
    
# print("Hello, I am nameless. How can I help you?")
engine.say("Hello, I am nameless. How can I help you?")
engine.runAndWait()

while True:
    audio = get_voice()
    # print(f">> {audio}")
    get_command(audio)