
#listen for the wake word jarvis
 #obtain audio from the microphone   
r = sr.Recognizer()
with sr.Microphone() as source:
print("listening...")
audio = r.listen(source, timeout=2, phrase_time_limit=1)

# recognize speech using Sphinx