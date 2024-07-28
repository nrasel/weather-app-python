import json
import pyttsx3
import requests


city=input("Enter the name of the city\n")
url=f"https://api.weatherapi.com/v1/current.json?key=3006278a5ed04499bb0173316242807&q={city}"

r=requests.get(url)
print(type(r.text))
wdic=json.loads(r.text)
print(type(wdic))
w=wdic["current"]["temp_c"]

engine = pyttsx3.init()
engine.say(f"The current weather in {city} is {w} degrees")
engine.runAndWait()