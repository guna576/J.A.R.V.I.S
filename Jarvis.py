# -*- coding: utf-8 -*-
"""
Created on Tue May 26 09:22:43 2020

@author: Gunashekar Chenna
"""
#download packages speechrecognition,wikipedia,pyttsx3 using PIP
import speech_recognition as sr
import pyttsx3
import os
import wikipedia
import webbrowser
import datetime

#Uses the voice 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

#sets the specified voice
engine.setProperty('voices',voices[0].id)

def speak(audio):
    #used to speak with the audio
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    #wishes in the begining
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('good morning sir!')
    else:
        speak('welcome back sir!')
    speak("what do u want sir" )
def takeCommand():
    
    r = sr.Recognizer()
    #listen the words
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        #chceks whether its a valid query  or not
        print("Recognizing ..")
        query = r.recognize_google(audio, language='en-in')
        print(f'You : {query}\n')
    except Exception as e:
        print(e)
        print("Sorry, please say that again..")
        return "NOne"
    return query

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower() 
        if 'wikipedia' in query:
            #speaak some name followed by wikipedia
            speak('Searching wikipedia')
            query = query.replace('wikipedia','')
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia..")
            print(result)
            speak(result)
         #speak accordingly as we intitialized the paths in our pc   
        elif "open YouTube" in query:
            
            webbrowser.open("https:\\www.youtube.com")
        elif "open google" in query:
            webbrowser.open("https:\\www.google.com")
        elif "open v s code" in query:
            codepath = r"C:\Users\Gunashekar Chenna\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codepath)


















        