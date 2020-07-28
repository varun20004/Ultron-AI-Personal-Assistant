import datetime
import os
import webbrowser
import wikipedia
import smtplib
import pythoncom
from tkinter import messagebox
from fileseletor import openFile
from test import *
from games import TIC_TAC_TOE
from ultron_functions import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
chatbot = ChatBot('Ultron1.1')
conv=open("C:/Users/varun sharma/Desktop/personal/AI Ultron personal assistant/memoreofchatbot.txt","r").readlines()
trainer = ListTrainer(chatbot)
trainer.train(conv)
print("Intilizing ultron..")
speak("Intilizing ultron..")
speak("how may i help you")
while True:
    query=TC()
    if query==None:
        pass
    elif "play game" in query:
        speak("Ok Sir..")
        TIC_TAC_TOE()
    elif 'Wikipedia' in query:
        query1=query.replace('Wikipedia','')
        f=open("C:/Users/varun sharma/Desktop/personal/AI Ultron personal assistant/memoreofchatbot.txt","a")
        f.write("tell me somthing about "+query1+"/n")
        speak("saerching wikipedia......")
        result=wikipedia.summary(query1,sentences=3)
        f.write(result+"/n")
        f.close()
        print(result)
        speak(result)
    elif "opne word" in query:
        w="C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE"
        os.startfile(w)
    elif "open command prompt" in query:
        os.system("cmd.exe")
    elif "open filmora" in query:
        f="C:/Program Files/Wondershare/Filmora9/Wondershare Filmora9.exe"
        os.startfile(f)
    elif "open android studio" in query:
        a="C:/Program Files/Android/Android Studio/bin/studio64.exe"
        os.startfile(a)
    elif "send an email" in query:
        speak("send eamil to whom...")
        peron=TC()
        if peron=="Varun Sharma" or "Varun":
            email="varunsharma20004@gmail.com"
            speak("What would be the subject of mail")
            subject=TC()
            speak("what should I write in body")
            massage=TC()
            speak("Do you want to add attachment")
            d=messagebox.askyesno("attechments","do you want to add attechments")
            if d == True:
                l=openFile()
                fl=l[0]
                y=len(fl)-1
                s=""
                while y!=0:
                    if fl[y]=="/":
                        break
                    else:
                        s=fl[y]+s
                        y=y-1
                emailscript(email,subject,massage,s,fl)
            else:
                emailscript1(email,subject,massage)
        if peron=="Mehul" or "Mehul Verma":
            email="mehulverma04@gmail.com"
            speak("What would be the subject of mail")
            subject=TC()
            speak("what should I write in body")
            massage=TC()
            speak("Do you want to add attachment")
            d=TC()
            if d == "yes":
                l=openFile()
                fl=l[0]
                y=len(fl)-1
                s=""
                while y!=0:
                    if fl[y]=="/":
                        break
                    else:
                        s=fl[y]+s
                        y=y-1
                emailscript(email,subject,massage,s,fl)
            elif d=="no":
                emailscript1(email,subject,massage)
        else:
            speak("use not found")
    elif 'open settings' in query:
        os.system('control.exe')
    elif 'open WhatsApp' in query:
        w="C:/Users/varun sharma/AppData/Local/WhatsApp/WhatsApp.exe"
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
    elif "search" in query :
        try:
            from googlesearch import search 
        except ImportError: 
	        print("No module named 'google' found") 
        for j in search(query, tld="co.in", num=10, stop=1, pause=2): 
            speak(f'opning {j}/n')
            webbrowser.open(j)
    elif "standby mode" in query:
        hold()
    else:
        response=chatbot.get_response(query)
        print(response)
        speak(response)