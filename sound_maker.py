import json, urllib.request
import webbrowser
import tkinter as tk # 1
from tkinter import ttk, Menu
from gtts import gTTS

#function imports from local directory
from NEWSaudio import googNews
from WEATHERaudio import weather

#tts = gTTS(text='Your computer needs more DAVID STRINGA', lang='en')
#tts.save("hello123.mp3")
desiredTracks = []

def addRemove(some_function):
    print("addRemove was called")
    if some_function in desiredTracks:
        print("removing...")
        desiredTracks.remove(some_function)
    else:
        print("adding...")
        desiredTracks.append(some_function)
    return

def makeAllSound():
    print("makeAllSound was called")
    for fn in desiredTracks:
        print("fn about to be called")
        fn()
    action1.configure(text='Sound file saved.')
    webbrowser.open("daNews.mp3") #Opens in OS's default mp3 player
    return


win = tk.Tk() # 2
win.title("Personal Sandbox") # 3

action1 = ttk.Button(win, text="Generate Audio", command=makeAllSound) # 7
action1.grid(column=0, row=0, padx=20, pady=10)

#webbrowser.open("futureReminders.txt") #Opens in OS's default .txt editor (Notepad)

num_of_choices = 2
checkInt = [] #This array will store all of our checkbox flags- no sense in creating individual variables
for i in range(num_of_choices):
    checkInt.append(tk.IntVar())
newsCheck = tk.Checkbutton(win, text="Google News", variable=checkInt[0], command=lambda: addRemove(googNews)) #Without the lambda, python evaluates the expression and stores the result in command instead of executing it as a callback
newsCheck.deselect()
newsCheck.grid(column=0, row=1, sticky=tk.W)

weatherCheck = tk.Checkbutton(win, text="Helsinki Weather", variable=checkInt[1], command=lambda: addRemove(lambda: weather("Helsinki"))) #Without the lambda, python evaluates the expression and stores the result in command instead of executing it as a callback
weatherCheck.deselect()
weatherCheck.grid(column=0, row=2, sticky=tk.W)

def _quit(): # 7
    win.quit()
    win.destroy()
    exit()

menuBar = Menu(win) # 1
win.config(menu=menuBar)
fileMenu = Menu(menuBar, tearoff=0) # 2
fileMenu.add_command(label="New")
fileMenu.add_command(label="Exit", command=_quit)
menuBar.add_cascade(label="File", menu=fileMenu)

helpMenu = Menu(menuBar, tearoff=0) # 6
helpMenu.add_command(label="About")
menuBar.add_cascade(label="Help", menu=helpMenu)

win.mainloop() # 4
