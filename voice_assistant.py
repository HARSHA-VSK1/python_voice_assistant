#code with harry jarvis project

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser 
import os
import requests
from bs4 import BeautifulSoup
import pandas
import pywhatkit
import smtplib

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("Good morning")

    elif hour >=12 and hour <18:
        speak("Good Afternoon")
    
    else:
        speak("good evening")
    
    speak("Hello this is jaya")


def takeCommand():
    #it takes microphone input
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold=500
        audio = r.listen(source)
    
    try:
        print("Recognizing..")
        query = r.recognize_google(audio,language='en-in')
        print("User said:", query)
    
    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    with open('pass.txt') as file:
        password = file.read()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('harshavsk2002@gmail.com',password)
    server.sendmail('harshavsk2002@gmail.com',to,content)
    server.close()

def google_query(quer):
    url=f"https://www.google.com/search?q={quer}"
    result=requests.get(url)
    data = BeautifulSoup(result.text,"html.parser")
    finres = data.find("div",class_='BNeawe').text
    return finres 


email_dict={'harry':'harshavsk2002@gmail.com','vsk':'saikirtanreddy@gmail.com','deadpool':'sairedz2002@gmail.com','vtr':'vtreddy02@gmail.com'}

if __name__=='__main__':
    wishme()

    while True:
        query = takeCommand().lower()
        #logic for executing task
        if 'wikipedia' in query:
            speak('Searching wikipedia')
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('https://www.youtube.com/')

        elif 'open google' in query:
            webbrowser.open('https://www.google.com/')
        
        elif 'open stack' in query:
            webbrowser.open('https://www.stackoverflow.com/')

        elif 'time' in query:
            strTime= datetime.datetime.now().strftime("%M:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open vs code' in query:
            path=r"C:\Users\V S K HARSHAVARDHAN\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(path)

        elif 'open harry' in query:
            webbrowser.open('https://www.youtube.com/c/CodeWithHarry')
        
        elif 'no way home' in query:
            webbrowser.open('https://www.youtube.com/results?search_query=no+way+home')

        elif 'search in youtube' in query:
            qu=takeCommand().lower()
            qustr = 'https://www.youtube.com/results?search_query='+qu
            webbrowser.open(qustr)
        
        elif 'search in google' in query:
            qu = query.replace('search in google ','')
            result = google_query(qu)
            webbrowser.open(f"https://www.google.com/search?q={qu}")
            print(result)
            speak(result)

        elif 'temperature' in query:
            result = google_query(query)
            speak(result)
        
        elif 'send email to' in query:
            try:
                key = query.replace('send email to ','')
                speak('what should i say')
                content = takeCommand()
                to = email_dict[key]
                sendEmail(to, content)
                speak('email is sent')
            
            except Exception as e:
                print(e)
                speak('sorry harsha email not sent')

        elif 'read csv' in query:
            file= takeCommand()
            try:
                file_name = file + '.csv'
                path  = r'C:\Users\V S K HARSHAVARDHAN\Desktop\assem\jarvis'
                ap = os.path.join(path,file_name)
                data = pandas.read_csv(ap)
                speak("The fields in this file are")
                for i in data.columns:
                    speak(i)
                #print(data.describe)
            except FileNotFoundError:
                speak("The file could not be found")
        
        elif 'play' in query:
            query = query.replace('play','')
            pywhatkit.playonyt(query)
        
        elif 'open lms' in query:
            webbrowser.open('https://learning.cbit.org.in/')
            
        elif 'bye' in query:
            speak('see you soon harsha')
            break;

        elif 'thank you jaya' in query:
            speak("Anything for u harsha")
            break;
