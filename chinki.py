import subprocess
import wolframalpha
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pyaudio
import webbrowser

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait( )
    
def wishMe( ):
    hour = int(datetime.datetime.now( ).hour)
    if hour>=0 and hour<12:speak("good morning")

    elif hour>=12 and hour<18:speak("good afternoon")
    else:
        speak("good night")

    speak("Chinki 1 point o I am your voice assistant Arya, how may I help you?")

def takeCommand( ):
    r=sr.Recognizer( )
    with sr.Microphone( ) as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print("Listening...")
        audio = r.listen(source)
        r.record(source, duration = 4, offset = None)
        
            
    try:
        print("You said")
        words=r.recognize_google(audio, language = 'en-in')
        print(f"User said: {words}\n")

    except LookupError:
        print(e)
        print("Say it again please")
        return "None"
    return words
    
if __name__=="__main__":
    
    wishMe( )
    
    while True:
        
        query = takeCommand( )
        
        if 'Wikipedia' in query:
            speak("Searching Wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            
        elif 'YouTube' in query:
            speak("Opening youtube\n")
            webbrowser.open("youtube.com")

        elif 'Google' in query:
            speak("Opening google\n")
            webbrowser.open("google.co.in")

        elif 'GitHub' in query:
            speak("Opening github\n")
            webbrowser.open("https://github.com/Ariyae")   

        elif 'Time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'How are you chinki' in query:
            speak("I am good")
            speak("What about you?")

        elif "Who i am" in query:
            speak("If you talk then definately you are human.")

        else:
            speak("My work is done")


    
