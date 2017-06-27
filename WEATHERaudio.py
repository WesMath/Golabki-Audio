import json, urllib.request
import webbrowser
import tkinter as tk # 1
from tkinter import ttk, Menu
from gtts import gTTS

def weather(city_name):
    print("weather was called")
    key = open('weather_api.txt', 'r')#Read API key from text file in directory (which git ignores)
    with urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q="+city_name+"&APPID="+key.read()) as url:
        data = json.loads(url.read().decode())
        output = "In "+city_name+", "+data['weather'][0]['description']+'.'
        output += "The temperature is "+ str(((9/5)*(float(data['main']['temp'])-273) + 32)) +" degrees Fahrenheit."
        #9/5 (K - 273) + 32 = Fahrenheit
        newsClip = gTTS(text=output, lang='en')
        newsClip.save(city_name+"Rain.mp3")
    return
