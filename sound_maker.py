import json, urllib.request
import webbrowser
import tkinter as tk # 1
from tkinter import ttk, Menu
from gtts import gTTS

#tts = gTTS(text='Your computer needs more DAVID STRINGA', lang='en')
#tts.save("hello123.mp3")
desiredTracks = []

def addRemove(some_function):
    print("addRemove was called")
    if some_function in desiredTracks:
        desiredTracks.remove(some_function)
    else:
        desiredTracks.append(some_function)
    return

def makeAllSound():
    print("makeAllSound was called")
    for fn in desiredTracks:
        print("fn about to be called")
        fn()
    return

def googNews():
    print("googNews was called")#TODO relocate global button GUI updating
    key = open('news_api.txt', 'r')
    with urllib.request.urlopen("https://newsapi.org/v1/articles?source=google-news&sortBy=top&apiKey="+key.read()) as url:
        data = json.loads(url.read().decode())
        output = ""
        for i in range(len(data['articles'])):
            output += ". Article Number " + str(i + 1) + ". " + data['articles'][i]['title']
        newsClip = gTTS(text=output, lang='en')
        newsClip.save("daNews.mp3")
        action1.configure(text='Sound file saved.')
        webbrowser.open("daNews.mp3") #Opens in OS's default mp3 player


win = tk.Tk() # 2
win.title("Personal Sandbox") # 3

action1 = ttk.Button(win, text="Generate Audio", command=makeAllSound) # 7
action1.grid(column=0, row=0, padx=20, pady=10)

#webbrowser.open("futureReminders.txt") #Opens in OS's default .txt editor (Notepad)

num_of_choices = 1
checkInt = [] #This array will store all of our checkbox flags- no sense in creating individual variables
for i in range(num_of_choices):
    checkInt.append(tk.IntVar())
newsCheck = tk.Checkbutton(win, text="Google News", variable=checkInt[0], command=lambda: addRemove(googNews)) #Without the lambda, python evaluates the expression and stores the result in command instead of executing it as a callback
newsCheck.select()
newsCheck.grid(column=0, row=1, sticky=tk.W)

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
