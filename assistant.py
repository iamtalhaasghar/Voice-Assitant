import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import datetime
import smtplib
import pyjokes
import pywhatkit
from email.message import EmailMessage
from plyer import notification  
from pynput.keyboard import Key,Controller

engine = pyttsx3.init()
#voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 120) # speed wp/m
emaillist = dict()

keyboard = Controller()


def notify(msg):
    return 
    notification_title = 'Your Voice Assistant'  
    notification_message = msg
      
    notification.notify(  
        title = notification_title,  
        message = notification_message,  
        app_icon = None,  
        timeout = 10,  
        toast = False  
        )  


def speak(sentence):
    engine.say(sentence)
    engine.runAndWait()


def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    file = open("password.txt", 'r')
    password = file.read()
    server.login(None, password)
    # server.sendmail(None, to, content)
    server.send_message(content)
    server.close()
    speak(f"Sent an email to {to} ")


def greetme():
    speak("How can I help you?")


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 0.5
        # r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        print("Recognizing")
        query = r.recognize_google(audio)
        print(f"You said: {query}")
        query = query.lower()
        if 'exit' in query:
            speak("Bye!")
            exit()
        else:
            query = query.replace("your assistant", "")

    except Exception as e:
        print("Couldn't recognize that, can you please repeat")
        #speak("Couldn't recognize that, can you please repeat")
        return "none"
    return query


if __name__ == "__main__":
    greetme()
    while True:
        query = takeCommand().lower()
    
        if 'wikipedia' in query:
            try:
                print("Searching....wait")
                query = query.replace("wikipedia", "")
                query = query.replace("according to", "")
                query = query.replace("who is", "")
                query = query.replace("what is", "")
                results = wikipedia.summary(query, sentences=1)
                speak("So wikipedia says  ")
                print(results)
                speak(results)
            except Exception as e:
                speak("Couldn't find that, sorry!")
                print("Couldn't find that")

        elif 'open browser' in query:
            browserpath = None
            speak("opening chrome")
            print("Opening chrome..")
            os.startfile(browserpath)

        elif 'open instagram' in query:
            speak("opening instagram")
            print("Opening instagram...")
            webbrowser.open('instagram.com')

        elif 'open youtube' in query:
            speak("starting youtube")
            print("Opening youtube...")
            webbrowser.open('youtube.com')

        elif 'open github' in query:
            speak("opening github")
            print("Opening github..")
            webbrowser.open('github.com')

        elif 'open google' in query:
            speak("opening google")
            print("Opening google...")
            webbrowser.open('google.com')

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)
            print(joke)
        elif 'play' in query:
            if 'play music' in query:
                print("Playing music...")
                speak("Playing music")
                music_dir = None
                songslist = os.listdir(music_dir)
                songlistlen = len(songslist) - 1
                r = random.randint(0, songlistlen)
                os.startfile(os.path.join(music_dir, songslist[r]))

            elif 'play songs' in query:
                print("Playing music...")
                speak("playing music")
                music_dir = None 
                songslist = os.listdir(music_dir)
                songlistlen = len(songslist) - 1
                r = random.randint(0, songlistlen)
                os.startfile(os.path.join(music_dir, songslist[r]))

            else:
                query = query.replace("play", "")
                speak(f"Playing {query}")
                print(f"Playing {query}")
                pywhatkit.playonyt(query)

        elif 'current time' in query:
            crnttime = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {crnttime}")
            print(f"The current time is {crnttime}")

        elif 'open torrent' in query:
            tpath = None 
            speak("Opening torrent")
            os.startfile(tpath)

        elif 'email to me' in query:
            try:
                speak("What should I put in the body of the mail?")
                content = takeCommand()
                to = None
                sendemail(to, content)
            except Exception as e:
                print(e)

        elif 'what is your story' in query:
            speak("My story according to netflix is")
            webbrowser.open('')

        elif 'send email' in query:
            try:
                    content = EmailMessage()
                    # speak("What should be the subject of the mail?")
                    # to set the subject
                    query = 'none'
                    while query == 'none':
                        speak("What should I put in the subject of the mail?")
                        query = takeCommand()
                        content['Subject'] = query

                    # to set the body
                    query = 'none'
                    while query == 'none':
                        speak("What should I put in the body of the mail?")
                        query = takeCommand()
                        content.set_content(query)

                    # to set the recipient
                    query = 'none'
                    content['From'] = None
                    while query == 'none':
                        speak("Who should be the recipient?")
                        rec = takeCommand().lower()
                        query = rec
                        try:
                            to = emaillist[rec]
                        except Exception as e:
                            print(e)
                            query = 'none'
                    content['To'] = to

                    # to send the actual email
                    sendemail(to, content)

            except Exception as e:
                    print(e)

                
        elif 'search' in query:
            query = query.replace("search", "")
            query = query.replace("about", "")
            query = query.replace("for", "")
            speak(f"searching {query}")
            pywhatkit.search(query)

        elif 'send an email' in query:
            try:
                content = EmailMessage()
                # speak("What should be the subject of the mail?")
                # to set the subject
                query = 'none'
                while query == 'none':
                    speak("What should I put in the subject of the mail?")
                    query = takeCommand()
                    content['Subject'] = query

                # to set the body
                query = 'none'
                while query == 'none':
                    speak("What should I put in the body of the mail?")
                    query = takeCommand()
                    content.set_content(query)

                # to set the recipient
                query = 'none'
                content['From'] = None
                while query == 'none':
                    speak("Who should be the recipient?")
                    rec = takeCommand().lower()
                    query = rec
                    try:
                        to = emaillist[rec]
                    except Exception as e:
                        print(e)
                        query = 'none'
                content['To'] = to

                # to send the actual email
                sendemail(to, content)

            except Exception as e:
                print(e)
        elif 'page' in query:
            if 'down' in query:
                keyboard.press(Key.page_down)
                keyboard.release(Key.page_down)
            if 'up' in query:
                keyboard.press(Key.page_up)
                keyboard.release(Key.page_up)
            
        else:
            if query != 'none':
                speak("I am not able to do that, sorry!")
