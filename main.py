from ultron_functions import *
import datetime
import os
import webbrowser
import wikipedia
import smtplib
import pythoncom
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
chatbot = ChatBot('Ultron1.1')
conv=open(r"C:\Users\varun sharma\Desktop\personal\AI Ultron personal assistant\memoreofchatbot.txt","r").readlines()
trainer = ListTrainer(chatbot)
trainer.train(conv)
print("Intilizing ultron..")
speak("Intilizing ultron..")
speak("how may i help you")
while True:
    query=TC()
    if query==None:
        pass
    if 'Wikipedia' in query:
        query1=query.replace('wikipedia','')
        f=open(r"C:\Users\varun sharma\Desktop\personal\AI Ultron personal assistant\memoreofchatbot.txt","a")
        f.write("tell me somthing about "+query1+"\n")
        speak("saerching wikipedia......")
        result=wikipedia.summary(query1,sentences=3)
        f.write(result+"\n")
        f.close()
        print(result)
        speak(result)
    elif 'tell me something about you' in query:
        speak('I am ultron an AI assistent created ny varun sharma I am sill not complet but my creator tride hard to reat me')
    elif 'tell me a joke' in query:
        print("Two boys were arguing when the teacher entered the room.") 
        print("The teacher says, 'Why are you arguing?'")
        print("One boy answers, 'We found a ten dollor bill and decided to give it to whoever tells the biggest lie.'")
        print('"You should be ashamed of yourselves," said the teacher, "When I was your age I didnt even know what a lie was."')
        print("The boys gave the ten dollars to the teacher.")
        speak("Two boys were arguing when the teacher entered the room. The teacher says, 'Why are you arguing?' One boy answers, 'We found a ten dollor bill and decided to give it to whoever tells the biggest lie.' 'You should be ashamed of yourselves,' said the teacher, 'When I was your age I didnt even know what a lie was.' The boys gave the ten dollars to the teacher.")
    elif 'open settings' in query:
        os.system('control.exe')
    elif 'open WhatsApp' in query:
        w="C:\\Users\\varun\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
        os.startfile(w)
    elif "goodbye" in query:
        speak("Good bye master")
        break
    elif 'time' in query:
        t = datetime.time()
        speak(t)
    elif "date" in query:
        now = datetime.datetime.now()
        print (now.strftime("%d-%m-%y"))
        speak (now.strftime("%d-%m-%y"))
    elif 'search' in query :
        try:
            from googlesearch import search 
        except ImportError: 
	        print("No module named 'google' found") 
        for j in search(query, tld="co.in", num=10, stop=1, pause=2): 
            speak(f'opning {j}\n')
            webbrowser.open(j)
    else:
        response=chatbot.get_response(query)
        print(response)
        speak(response)