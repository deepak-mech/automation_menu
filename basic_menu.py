import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random

print("\n\t\t\t----------------->Your welcome in this Basic Automation Menu Program<----------------\t\t\n") 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning')

    elif hour>=12 and hour<18:
        speak('Good Afternoon') 
        
    else:
        speak('Good Night')

    speak('Sir, Ziara here, Please tell me how may I help you?')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\t\tI am listening....\n")
        speak(" Tell me your requirements......")
        r.pause_threshold = 1 
        audio = r.listen(source)
      

    try:
        print('\t\tRecognising....\n')
        speak("I got it, please wait.....")
        query = r.recognize_google(audio, language='en-in')
        #print(query)

    except Exception as e:
        print(e)
        print('Say that again please...')
        return 'None'

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mrdeepakshah3076@gmail.com', '445651@#') 
    server.sendmail('mrdeepakshah3076@gmail.com', to, content) 
    server.close()        

if __name__ == "__main__":
    wishMe()
    while True: 
        os.system('cls')   
        print("\n\t\t\t----------------->Your welcome in this Basic Automation Menu Program<----------------\t\t\n\n") 
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'how are you' in query:
            speak('Sir, I am fine whats abut you')

        elif 'wikipedia' in query:
            speak('Searching wikipedia....')
            query = query.replace('wikipedia', '') 
            results = wikipedia.summary(query, sentences = 1)
            speak('According to wikipedia')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stack overflow' in query:
            webbrowser.open('stackoverflow.com')

        
        elif "date" in query:
            webbrowser.open("http://192.168.43.146/cgi-bin/iiec.py?x=date")

        elif  "calendar"  in query:
	        webbrowser.open("http://192.168.43.146/cgi-bin/iiec.py?x=cal")

        elif 'play music' in query:
            Videoder = 'C:\\Users\\sargam\\Desktop\\Videoder'
            songs = os.listdir(Videoder)
            # print(songs)
            os.startfile(os.path.join(Videoder, songs[random.randrange(0, 10)]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Sir, the time is {strTime}')
            print(f'Sir, the time is {strTime}')

        elif 'open vs code' in query:
            vsCodePath = "C:\\Users\\sargam\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vsCodePath)

        elif 'open pycharm' in query:
            PyChm = "C:\\Program Files\\JetBrains\PyCharm Community Edition 2020.1\\bin\\pycharm64.exe"
            os.startfile(PyChm)

        elif 'open oracle virtual box' in query:
            oracleVB = "C:\\Program Files\\Oracle\\VirtualBox\\VirtualBox.exe"
            os.startfile(oracleVB)

        
        elif 'open teamviewer' in query:
            tmViewer = "C:\\Program Files (x86)\\TeamViewer\\TeamViewer.exe"
            os.startfile(tmViewer)

        elif  (("run" in query) or  ("execute" in query) or ('open' in query ))  and ("chrome" in query):
            os.system("chrome")

        elif  (("run" in query) or ("execute" in query) or ('open' in query)) and (("notepad" in query) or ("editor" in query)):
 	        os.system("notepad")

        elif  (("run" in query) or ("execute" in query) or ('open' in query)) and ("media" in query) and ("player" in query):
            os.system("wmplayer")

        elif "network configuration" in query:
            os.system("ipconfig")

        elif 'email to deepak' in query:
            # To send the email you must have to turn on less secure apps ON first in your gogle account.
            try:
                speak('What should I say?')
                content = takeCommand()
                to = 'mrdeepakshah3076@gmail.com'
                sendEmail(to, content)
                speak('Email has been sent!')

            except Exception as e:
                print(e)
                speak('Sorry sir, I am not able to send the email at this moment')

        elif 'exit' in query:
            print('Thankyou sir for using my services')
            break

        input(" Please enter to continue......")

             
   

      




