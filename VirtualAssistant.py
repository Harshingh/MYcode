import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
#print(voices)
engine.setProperty('voices',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good evening!")

    speak("Hey i am Jarvis,How can i help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)

        print("Could you please repeat...")
        return "None"
    return query

if __name__ == "__main__":
    wishme()
while True:
    query = takeCommand().lower()

    if 'wikipedia' in query:
        speak('Searching Wkikipedia')
        query = query.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        print(result)
        speak(result)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M")
        speak(f"Sir, the time is{strTime}")

    elif 'open vs code' in query:
        codepath = "C:\\Users\\Harshvardhan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codepath)
    
    elif 'repeat' in query:
        speak(query)