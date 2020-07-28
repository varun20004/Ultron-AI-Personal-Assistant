import tkinter as tk
from tkinter import *
from tkinter import messagebox as MB
import random
def TIC_TAC_TOE():
    #surface where we are going to create grid for game
    box=tk.Tk()
    box.geometry("500x500")
    box.title("TIC TAC TOE")
    box.resizable(0,0)
    #global variables
    r1=["0","0","0"]
    r2=["0","0","0"]
    r3=["0","0","0"]
    #all the def for program
    def box10():
        pass
    def notblank():
        l=[1,2,3,4,5,6,7,8,9]
        run=True
        while run:
            d=random.sample(l,1)
            if d[0]==1 and r1[0]=="0":
                box1.configure(text="X")
                box1.configure(fg="red")
                box1.configure(command=box10)
                r1.pop(0)
                r1.insert(0,"X")
                run=False
            elif d[0]==2 and r1[1]=="0":
                box2.configure(text="X")
                box2.configure(fg="red")
                box2.configure(command=box10)
                r1.pop(1)
                r1.insert(1,"X")
                run=False
            elif d[0]==3 and r1[2]=="0":
                box3.configure(text="X")
                box3.configure(fg="red")
                box3.configure(command=box10)
                r1.pop(2)
                r1.insert(2,"X")
                run=False
            elif d[0]==4 and r2[0]=="0":
                box4.configure(text="X")
                box4.configure(fg="red")
                box4.configure(command=box10)
                r2.pop(0)
                r2.insert(0,"X")
                run=False
            elif d[0]==5 and r2[1]=="0":
                box5.configure(text="X")
                box5.configure(fg="red")
                box5.configure(command=box10)
                r2.pop(1)
                r2.insert(1,"X")
                run=False
            elif d[0]==6 and r2[2]=="0":
                box6.configure(text="X")
                box6.configure(fg="red")
                box6.configure(command=box10)
                r2.pop(2)
                r2.insert(2,"X")
                run=False
            elif d[0]==7 and r3[0]=="0":
                box7.configure(text="X")
                box7.configure(fg="red")
                box7.configure(command=box10)
                r3.pop(0)
                r3.insert(0,"X")
                run=False
            elif d[0]==8 and r3[1]=="0":
                box8.configure(text="X")
                box8.configure(fg="red")
                box8.configure(command=box10)
                r3.pop(1)
                r3.insert(1,"X")
                run=False
            elif d[0]==9 and r3[2]=="0":
                box9.configure(text="X")
                box9.configure(fg="red")
                box9.configure(command=box10)
                r3.pop(2)
                r3.insert(2,"X")
                run=False
    def win():
        global r1,r2,r3
        p1=["O","O","O"]
        p2=["X","X","X"]
        a1=[r1[0],r2[0],r3[0]]
        a2=[r1[1],r2[1],r3[1]]
        a3=[r1[2],r2[2],r3[2]]
        a4=[r1[0],r2[1],r3[2]]
        a5=[r1[2],r2[1],r3[0]]
        if r1==p1 or r2==p1 or r3==p1 or a1==p1 or a2==p1 or a3==p1 or a4==p1 or a4==p1 or a5==p1:
            MB.showinfo("Game over","You win")
            a=MB.askquestion("New Game","Do You want to Play Again")
            if a=="No":
                box.destroy()
            else :
                r1=["0","0","0"]
                r2=["0","0","0"]
                r3=["0","0","0"]
                box1.configure(text="  ")
                box1.configure(command=box1)
                box2.configure(text="  ")
                box2.configure(command=b2)
                box3.configure(text="  ")
                box3.configure(command=b3)
                box4.configure(text="  ")
                box4.configure(command=b4)
                box5.configure(text="  ")
                box5.configure(command=b5)
                box6.configure(text="  ")
                box6.configure(command=b6)
                box7.configure(text="  ")
                box7.configure(command=b7)
                box8.configure(text="  ")
                box8.configure(command=b8)
                box9.configure(text="  ")
                box9.configure(command=b9)
        elif r1==p2 or r2==p2 or r3==p2 or a1==p2 or a2==p2 or a3==p2 or a4==p2 or a4==p2 or a5==p2:
            MB.showinfo("Game over","You lose")
            a=MB.askquestion("New Game","Do You want to Play Again")
            if a=="No":
                box.destroy()
            else :
                r1=["0","0","0"]
                r2=["0","0","0"]
                r3=["0","0","0"]
                box1.configure(text="  ")
                box1.configure(command=box1)
                box2.configure(text="  ")
                box2.configure(command=b2)
                box3.configure(text="  ")
                box3.configure(command=b3)
                box4.configure(text="  ")
                box4.configure(command=b4)
                box5.configure(text="  ")
                box5.configure(command=b5)
                box6.configure(text="  ")
                box6.configure(command=b6)
                box7.configure(text="  ")
                box7.configure(command=b7)
                box8.configure(text="  ")
                box8.configure(command=b8)
                box9.configure(text="  ")
                box9.configure(command=b9)
        else :
            for x in range(0,1):
                s=""
                for y in range (0,3):
                    r=[r1,r2,r3]
                    for z in range(0,3):
                        h=r[y]
                        s=s+h[z]
            if "0" in s:
                pass
            else:
                print("drew")
    def b1():
        box1.configure(text="O")
        box1.configure(fg="blue")
        box1.configure(command=box10)
        r1.pop(0)
        r1.insert(0,"O")
        if r3[2]=="0":
            box9.configure(text="X")
            box9.configure(fg="red")
            box9.configure(command=box10)
            r3.pop(2)
            r3.insert(2,"X")
        else:
            notblank()
        win()
    def b2():
        box2.configure(text="O")
        box2.configure(fg="blue")
        box1.configure(command=box10)
        r1.pop(1)
        r1.insert(1,"O")
        if r3[1]=="0":
            box8.configure(text="X")
            box8.configure(fg="red")
            box8.configure(command=box10)
            r3.pop(1)
            r3.insert(1,"X")
        else:
            notblank()
        win()
    def b3():
        box3.configure(text="O")
        box3.configure(fg="blue")
        box3.configure(command=box10)
        r1.pop(2)
        r1.insert(2,"O")
        if r3[0]=="0":
            box7.configure(text="X")
            box7.configure(fg="red")
            box7.configure(command=box10)
            r3.pop(0)
            r3.insert(0,"X")
        else:
            notblank()
        win()
    def b4():
        box4.configure(text="O")
        box4.configure(fg="blue")
        box4.configure(command=box10)
        r2.pop(0)
        r2.insert(0,"O")
        if r2[2]=="0":
            box6.configure(text="X")
            box6.configure(fg="red")
            box6.configure(command=box10)
            r2.pop(2)
            r2.insert(2,"X")
        else:
            notblank()
        win()
    def b5():
        box5.configure(text="O")
        box5.configure(fg="blue")
        box5.configure(command=box10)
        r2.pop(1)
        r2.insert(1,"O")
        notblank()
    def b6():
        box6.configure(text="O")
        box6.configure(fg="blue")
        box6.configure(command=box10)
        r2.pop(2)
        r2.insert(2,"O")
        if r2[0]=="0":
            box4.configure(text="X")
            box4.configure(fg="red")
            box4.configure(command=box10)
            r2.pop(0)
            r2.insert(0,"X")
        else:
            notblank()
        win()
    def b7():
        box7.configure(text="O")
        box7.configure(fg="blue")
        box7.configure(command=box10)
        r3.pop(0)
        r3.insert(0,"O")
        if r1[2]=="0":
            box3.configure(text="X")
            box3.configure(fg="red")
            box3.configure(command=box10)
            r1.pop(2)
            r1.insert(2,"X")
        else:
            notblank()
        win()
    def b8():
        box8.configure(text="O")
        box8.configure(fg="blue")
        box8.configure(command=box10)
        r3.pop(1)
        r3.insert(1,"O")
        if r1[1]=="0":
            box2.configure(text="X")
            box2.configure(fg="red")
            box2.configure(command=box10)
            r1.pop(1)
            r1.insert(1,"X")
        else:
            notblank()
        win()
    def b9():
        box9.configure(text="O")
        box9.configure(fg="blue")
        box9.configure(command=box10)
        r3.pop(2)
        r3.insert(2,"O")
        if r1[0]=="0":
            box1.configure(text="X")
            box1.configure(fg="red")
            box1.configure(command=box10)
            r1.pop(0)
            r1.insert(0,"X")
        else:
            notblank()
        win()
    #all the GUI and button for game
        #rows
    row1=Frame(box)
    row1.pack(expand=True,fill="both")
    row2=Frame(box)
    row2.pack(expand=True,fill="both")
    row3=Frame(box)
    row3.pack(expand=True,fill="both")
        #boxes
            #row1
    box1=Button(row1,text="  ",font=("Verdana",40),border=10,bg="white",command=b1)
    box1.pack(side="left",expand=True,fill="both")
    box2=Button(row1,text="  ",font=("Verdana",40),border=10,bg="white",command=b2)
    box2.pack(side="left",expand=True,fill="both")
    box3=Button(row1,text="  ",font=("Verdana",40),border=10,bg="white",command=b3)
    box3.pack(side="left",expand=True,fill="both")
            #row2
    box4=Button(row2,text="  ",font=("Verdana",40),border=10,bg="white",command=b4)
    box4.pack(side="left",expand=True,fill="both")
    box5=Button(row2,text="  ",font=("Verdana",40),border=10,bg="white",command=b5)
    box5.pack(side="left",expand=True,fill="both")
    box6=Button(row2,text="  ",font=("Verdana",40),border=10,bg="white",command=b6)
    box6.pack(side="left",expand=True,fill="both")
            #row3
    box7=Button(row3,text="  ",font=("Verdana",40),border=10,bg="white",command=b7)
    box7.pack(side="left",expand=True,fill="both")
    box8=Button(row3,text="  ",font=("Verdana",40),border=10,bg="white",command=b8)
    box8.pack(side="left",expand=True,fill="both")
    box9=Button(row3,text="  ",font=("Verdana",40),border=10,bg="white",command=b9)
    box9.pack(side="left",expand=True,fill="both")

    box.mainloop()