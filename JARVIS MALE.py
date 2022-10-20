import pyttsx3 
import speech_recognition as sr 
import datetime
import webbrowser
import os
import smtplib
import requests
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def remove(string):
    return string.replace(" ", "")

def weather(city):
    pi_key = "AAAAPPPPIIII_____KKKKEEEEYYYY"  # Enter the API key you got from the OpenWeatherMap website
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + city
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        z = x["weather"]

        weather_description = z[0]["description"]
        print (" Temperature (in celsius) = " + str(current_temperature) +"\n description = " + str(weather_description))
        s = (" Temperature (celsius) = " + str(current_temperature) +"\n description = " + str(weather_description))

    else:
        print(" City Not Found ")
        s = "city not found "

    return s 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hello Everyone!!!! This is JARVIS , Jatin sir personal Assistant . Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        
        elif 'youtube' in query:
            speak('opening youtube')
            webbrowser.open("youtube.com")
            time.sleep(10)


        elif 'stackoverflow' in query:
            speak('opening stackflow')
            webbrowser.open("stackoverflow.com")
            time.sleep(10)

        elif 'call ' in query:
            speak('doing video call whom so you want though duo')
            webbrowser.open("https://duo.google.com/?web&utm_source=marketing_page_button_top")
            time.sleep(10)

        elif 'play music' in query:
            speak('playing music')
            music_dir = 'D:\Song'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
            time.sleep(10)

        elif 'time' in query:
            speak('telling the time')
            strTime = datetime.datetime.now().strftime("%H:%M")    
            speak(f"Sir, the time is {strTime}")

        elif 'weather' in query:
            speak ('telling weather at anywhere you say')
            speak('tell the place ')
            city = takeCommand().lower()
            read = weather(city)
            speak ("today weather for the {city} is {read}")

        elif 'friend zone' in query:
            speak('Hi! everyone I am jatin sir personal assistant ')
            speak('everyone please tell your name ?')
            friend= takeCommand().lower()
            speak("Hi! sir welcome to jatin sir office")
            
        elif 'google' in query :
            speak ('ok sir just a minute what do you want to know ! ')
            query = takeCommand().lower()
            query = remove(query)
            webbrowser.open(f"https://www.google.com/search?q={query}")
            time.sleep(20)
            
            
        elif 'bye bye' in query:
            speak ('bye bye sir call whenever you want me')
            break;
