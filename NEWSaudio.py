import json, urllib.request
import webbrowser
import tkinter as tk # 1
from tkinter import ttk, Menu
from gtts import gTTS

def googNews():
    print("googNews was called")
    key = open('news_api.txt', 'r')#Read API key from text file in directory (which git ignores)
    with urllib.request.urlopen("https://newsapi.org/v1/articles?source=google-news&sortBy=top&apiKey="+key.read()) as url:
        data = json.loads(url.read().decode())
        output = ""
        for i in range(len(data['articles'])):
            output += ". Article Number " + str(i + 1) + ". " + data['articles'][i]['title']
        newsClip = gTTS(text=output, lang='en')
        newsClip.save("daNews.mp3")
