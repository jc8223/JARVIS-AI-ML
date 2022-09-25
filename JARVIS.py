import pyttsx3 
import speech_recognition as sr 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print ("listening.........")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print ("Recognize......")
            query = comand.reconize.google(audio, language= 'en-in')
            print (f"you said: {query}")

        except exception as error:
            return None

    return query

speak ("hey i using whatsapp")
takecommand()
    
