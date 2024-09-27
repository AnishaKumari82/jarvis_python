import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary


recognizer = sr.Recognizer()
engine = pyttsx3.init() 
#pip install pocketsphinx

def speak (text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link) 

    

if __name__ =="__main__":
    speak("initialising jarvis...    ")   
    
    while True:
        
                #listen for the wake word jarvis
                #obtain audio from the microphone   
        r = sr.Recognizer()
        
                    # recognize speech using Sphinx
        print("recognising...")
        try:
            with sr.Microphone() as source:
                print("listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)

            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("yaa")

                #listen for command

                with sr.Microphone() as source:
                    print("jarvis active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
            
        except Exception as e:
           print("Error; {0}".format(e))
        