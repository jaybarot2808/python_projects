import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import os
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print("Maria: ", audio)
  
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if True:
        speak("Welcome Back sir!")
        speak("How may I help you sir!")

def takecommand():
    r = sr.Recognizer() #Speech recognition means that when humans are speaking, a machine understands it. Here we are using Google Speech API
                        # in Python to make it happen. We need to install the following packages for this − Pyaudio 
    with sr.Microphone()as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)  #adjust_for_ambient_noise(source, duration = 1) Adjusts the energy threshold dynamically using audio from source 
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You: {query}\n")
        
       
    except Exception as e:
        print(e)
        print("Sorry I didnt get that , Please say that again")
        speak("Sorry I didnt get that , Please say that again")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()  #lower means here to take query in lower-case alphabets

        if 'wikipedia' in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            print("opening youtube....")
            speak("opening youtube....")
            webbrowser.open("https:\\www.youtube.com")

        elif 'open google' in query:
            print("opening google....")
            speak("opening google....")
            webbrowser.open("https:\\www.google.com")

        elif 'play music' in query:
            print("opening spotify....")
            speak("opening spotify....")
            webbrowser.open("https:\\www.spotify.com")
        elif 'hello' in query:
            print('Hello!')  
            speak("Hello!")
        elif 'goodbye' in query:
            print('See you later!')  
            speak('See you later!')
        elif 'what is your age' in query:
            print('19 years!')  
            speak('19 years!')
        elif 'what is your name' in query:
            print("I'm Maria the AI assistant of Jay!")  
            speak("I'm Maria the AI assistant of Jay!")
        elif 'i want to buy something' in query:
            print('If you want to buy something than search on google or go to amazon or flipkart or anyother e-commerce app.')  
            speak('If you want to buy something than search on google or go to amazon or flipkart or anyother e-commerce app.')
        elif 'what are you doing' in query:
            print('I am free i was made for your for your help!')  
            speak("I am free i was made for your for your help!")
        elif 'when are you available' in query:
            print('24/7 i am every time available for your help')  
            speak('24/7 i am every time available for your help')
        elif 'what is coding' in query:
            print('Programming, coding or software development, means writing computer code to automate tasks.')  
            speak('Programming, coding or software development, means writing computer code to automate tasks.')
        elif 'how can i learn programming' in query:
            print('Check out the some YouTube channels like code with harry,freecodecamp etc. or you can learn from different websites also.')  
            speak('Check out the some YouTube channels like code with harry,freecodecamp etc. or you can learn from different websites also.')