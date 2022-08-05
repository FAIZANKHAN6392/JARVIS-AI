import email
from http import server
from unittest import result
from winreg import QueryInfoKey
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
            speak("good morning!")
            
    elif hour>=12 and hour<18:
            speak("Good afternoon!")
            
    else:
            speak("Good Evening!")
            
    speak("I am jarvis. Please tell me how I help You")

def takecommand():
        #it takes microphone input from the user and returns string output
        
        r = sr.Recognizer()
        with sr.Microphone() as source:
                print("listening...")
                r.pause_threshold = 1
                audio = r.listen(source)
                
        try:
            print("recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said:{query}\n")
            
        except Exception as e:
             #print(e)
             print("say that again please...")
             return "None"
        return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yaman.pli@gmail.com', 'engineerfaizankhan@1')
    server.sendmail('yaman.pli@gmail.com', to, content)
    server.close()
if __name__== "__main__":
    wishMe()
    while True:
    #if 1:
            query = takecommand().lower()
            
            #Logic for excecuting task based on query
            if 'wikipedia' in query:
                    speak('Searching Wikipedia')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to wikipedia")
                    print(results)
                    speak(results)
                    
            elif 'open youtube' in query:
                    webbrowser.open("youtube.com")
                    
            elif 'open google' in query:
                    webbrowser.open("google.com")
                
            elif 'open stackoverflow' in query:
                    webbrowser.open("stackoverflow.com")
                    
            elif 'play music' in query:
                  music_dir = 'D:\\Non criteria\\songs\\Favorites Songs2'
                  songs = os.listedir(music_dir)
                  print(songs)
                  os.startfile(os.path.join(music_dir, songs[0]))
                  
            elif 'the time' in query:
                 strTime = datetime.datetime.now().strftime("%H:%M:%S")
                 speak(f"Sir, the time is {strTime}")
                 
            elif'open code' in query:
                    codePath = "C:\\Users\\yaman\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(codePath)
                    
            elif 'email to harry' in query:
                 try:
                     speak("what should I say?")
                     content = takecommand()
                     to = "yaman.pli@gmail.com"
                     sendEmail(to, content)
                     speak("Email has been sent !")
                 except Exception as e:
                     print(e)
                     speak("Sorry my friend faizan bhai. i am not able to send this email")
                        
                     
                     
                