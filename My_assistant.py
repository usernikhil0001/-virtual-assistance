import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from googletrans import Translator
import openai

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
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

        speak("Hi I am Nik, version two point O, speed one Terahertz and memory one zettabyte, May i help you")

def takeCommand():
    #it takes microphone input form the user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:  {query}/n")

    except Exception as e:
        #  print(e)

         print("Say that again please...")
         
         return "None"    
    return query
           
if __name__ == "__main__":
    wishMe()
    while True:
#     if 1:
        query = takeCommand() .lower()

        # logic for the exicuting task perform on query
        if 'wikipedia' in query:
             speak('Searching Wikipedia....')
             query = query.replace("wikipedia", "")
             results = wikipedia.summary(query, sentences=5)
             speak("According to wikipedia")
             print(results)
             speak(results)
             

        elif 'open youtube'in query:
             webbrowser .open("https://www.youtube.com/")
             speak('opening youtube')

        elif 'open google'in query:
             webbrowser .open("www.google.com")
             speak('opening google') 

        elif 'open stackoverflow'in query:
             webbrowser .open("stackoverflow.com")   
             
        elif 'the time'in query:
             strTime = datetime.datetime.now().strftime("%H:%M:%S")
             print(strTime)
             speak(f"Sir, the time is {strTime}")

        elif 'how are you'in query:
             print("I am fine, and you ?")
             speak(f"I am fine, and you")

        elif 'i am also fine'in query:
             print("i am glad, to hear it...")
             speak("i am glad, to hear it...")   

        elif 'did you eat'in query:
             print("i am fully charged now, now i am ready to help?")
             speak("i am fully charged now, now i am ready to help?")

        elif 'nik shutdown my pc'in query:
             speak("shutting down")
             os.system('shutdown -s')

        elif 'open my instagram'in query:
             webbrowser .open("https://www.instagram.com")
             print("opening your instagram wait sir")
             speak("opening your instagram sir...") 

        elif 'open my facebook'in query:
             webbrowser .open("https://www.facebook.com/")
             print("opening your facebook sir")
             speak("opening your facebook sir")

        elif 'open my website'in query:
             webbrowser.open("https://nassoftech.lapmates.com/")
             print("opening your website sir")
             speak("opening your website sir")

        elif "what's going on"in query:
             print("Nothing special, I'm working with my boss!")  
             speak("Nothing special, I'm working with my boss!")  

        elif "good night"in query:
             print("good night boss")
             speak("good night boss") 

        elif "best computer institute in the area"in query:
             print("Khushi Computer Institute is the best computer education institute in the area.")
             speak("Khushi Computer Institute is the best computer education institute in the area.")  

        elif "do you love me"in query:
             print("yes , your are my best friend and i love you too.")
             speak("yes , your are my best friend and i love you too.")

        elif "who is nikhil singh"in query:
             print("Nikhil Singh is a software engineer, as well as a skilled, developer")  
             speak("Nikhil Singh is a software engineer, as well as a skilled, developer")  

        elif "who are you"in query:
             print("Hi I am Nik, speed one Terahertz and memory one zettabyte, thank you, what is your good name")
             speak("Hi I am Nik, speed one Terahertz and memory one zettabyte, thank you, what is your good name")  

        elif "hi i am"in query:
             print("hi gentleman, nice to meet you")
             speak("hi gentleman, nice to meet you")      

        elif "sing a poem for me"in query:
             print("Twinkle, twinkle, little star, How I wonder what you are, Up above the world so high, Like a diamond in the sky, Twinkle twinkle little star, How I wonder what you are, When the blazing sun is gone, When he nothing shines upon, Then you show your little light, Twinkle, twinkle, all the night, Twinkle twinkle, little star, How I wonder what you are")
             speak("Twinkle, twinkle, little star, How I wonder what you are, Up above the world so high, Like a diamond in the sky, Twinkle twinkle little star, How I wonder what you are, When the blazing sun is gone, When he nothing shines upon, Then you show your little light, Twinkle, twinkle, all the night, Twinkle twinkle, little star, How I wonder what you are")

        elif "who is your boss"in query:
             print("my boss is Er Nikhil singh")
             speak("my boss is Er Nikhil singh")  

        elif "do you know nikhil singh"in query:
             print("yes, nikhil singh is the my boss")
             speak("yes, nikhil singh is the my boss")  

        elif "who is rudransh singh"in query:
             print("rudransh singh is the mental") 
             speak("rudransh singh is the mental")  

        elif "father of python"in query:
             print("")    



       



               
                  
                  
    









