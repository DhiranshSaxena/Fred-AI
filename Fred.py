import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pywhatkit as kit
import requests
from bs4 import BeautifulSoup

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


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

    speak("I am Fred Sir. Please tell me how may I help you. These are the following things that I can do.")
    print("1. Search Anything On WikiPedia\n2. Open YouTube\n3. Open Google\n4. Open StackOverflow\n5. Play Songs of your Choice\n6. Search Anything on Internet\n7. Tell you temperature of Anywhere\n8. Tell you the time\n9. E-Mail Someone \n10. Open My Code\n\n You can shut down me by Saying Close Fred")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    working = True
    while working:
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

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play' in query:
            query = query.replace("play", "")
            speak(f"Now, Playing {query}")
            kit.playonyt(query)

        elif 'search' in query:
            query = query.replace("search", "")
            speak(f"Now, Searching {query}")
            kit.search(query)

        elif 'close' in query:
            speak(f"Thank You Sir for allowing me to help!")
            working = False

        elif 'temperature' in query:
            query = query.replace("What is", "")
            url = f"https://www.google.com/search?q={query}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"Current {query} is {temp}")

        elif 'internet speed' in query:
            query = query.replace("What is", "")



        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "D:\\my_codes\\Projects\\Applications\\Python\\IoT\\Fred.py"
            os.startfile(codePath)

        elif 'email to siddhant' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "onedimension4@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir. I am not able to send this email")    