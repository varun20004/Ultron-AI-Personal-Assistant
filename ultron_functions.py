import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(text):
     engine.say(text)
     engine.runAndWait()
def TC():
    r=sr.Recognizer()                                                           
    with sr.Microphone() as source:
        speak("Listening...")
        print("Listening...")
        audio = r.listen(source,phrase_time_limit=3)
    try :
        print('Recognizing...')
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
    except :
        speak("say that again")
        query=None
    return query

def hold():
    w=True
    while w:
        r=sr.Recognizer()                                                           
        with sr.Microphone() as source:
            print("l")
            audio = r.listen(source, phrase_time_limit=5)
        try :
            print("r")
            query=r.recognize_google(audio,language='en-in')
            print(query)
            if "Ultron"==query:
                print("y")
                w=False
            else:
                print("n")
                continue
        except :
            print("f")
            continue