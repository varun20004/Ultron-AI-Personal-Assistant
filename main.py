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
conv=open(r"memoreofchatbot.txt","r").readlines()
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
        f=open(r"memoreofchatbot.txt","a")
        f.write("tell me somthing about "+query1+"\n")
        speak("saerching wikipedia......")
        result=wikipedia.summary(query1,sentences=3)
        f.write(result+"\n")
        f.close()
        print(result)
        speak(result)
    elif 'tell me something about you' in query:
        speak('I am ultron an AI assistent created ny varun sharma I am sill not complet but my creator tride hard to reat me')
    elif 'open settings' in query:
        os.system('control.exe')
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
