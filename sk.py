import pyttsx3
import datetime
import speech_recognition as sa
import wikipedia
import os
import webbrowser

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def bye():
    speak("bye sir")
    quit()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good moring")

    if hour>=12 and hour<18:
        speak("good afternoon")

    if hour>=18 and hour<=24:
        speak("good evening")

    speak("i am cc how can i help you")

def takecommand():
    r = sa.Recognizer()
    with sa.Microphone() as source:
        print("listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
       query = r.recognize_google(audio, language = "en_in, hindi, punjabi")
       print (query)
         
        

    except Exception as e:


        return "takecommand()"
    return query


        

if __name__=="__main__":
    wishMe()
    

    while True:
       query = takecommand().lower()

       if "search" in query:
        speak("searching it...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("according to search")
        speak(results)

       if "open youtube" in query:
        speak("opening")
        webbrowser.open("youtube.com")
        
        
       if "who are you" in query:
        speak("i am controller of code also known as cc who is invented by shivam attar on 5:13 pm in batala")
       
       if "how are you" in query:
        speak("i am fine and you")

       if "me too" in query:
        speak("it's good")

       if "i am also fine" in query:
        speak("that's good")

       if "i am also good" in query:
        speak("it's good")

       if "i am good" in query:
        speak("it's good")

       if "change voice id zero" in query:
        speak("ok i am changing it")
        engine.setProperty("voice", voices[1].id)

       if "change voice id one" in query:
        speak("ok i am changing it")
        engine.setProperty("voice", voices[0].id)

       if "open vs code" in query:
        speak("opening")
        co = "C:\\Users\\AVN\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(co)  

       if "open chrome" in query:
        speak("opening")
        ce = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(ce) 

       if "open photoshop" in query:
        speak("opening")
        ce = "C:\\Program Files (x86)\\Adobe\\Photoshop 7.0\\Photoshop.exe"
        os.startfile(ce) 

       if "where are you from" in query:
        speak("i'm from India")

       if "what's your dream" in query:
        speak("actually i want to become a cricketer but now in this stage i am your assistant and i want to help you anywhere you want")

       if "who is shivam attar" in query:
        speak("he is my master and due him i am talking with you")

       if "your birthdate" in query:
        speak("i was born on 27th december in year 2022 on that day it was a superior cold day")

       if "shut down" in query:
        c = "C:\\Windows\\System32\\slidetoShutDown.exe"
        os.startfile(c)
        bye()         

    
        

       if "bye" in query:
        bye() 

