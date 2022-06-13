import pyttsx3
from Math import mat
from requests import *
from json import *
from random import *
from re import *
import speech_recognition as sr
import time

# ecapture import ecapture as ec
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[10].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()


def weather_data():
    weather_params = {
        "lat": 30.542959,
        "lon": -97.547089,
        "appid": "33b074f8bf9edd2371e1afd2172333b8",
        "exclude": "Hourly, minutely, daliy"

    }
    response = get(url="http://api.openweathermap.org/data/2.5/onecall", params=weather_params)
    return response.json()


def speak_weather():
    data = weather_data()
    data_per_hour = data["daily"]

    return data_per_hour



from datetime import datetime

global name
name = ""

on_greet = False


def setup():
    global name
    names = input("What is your name?\n")
    name = names


def greet():
    global name
    text = datetime.today().strftime("%I:%M %p")
    if "AM" in text:
        speak(f"Good morning {name}")
    elif "PM" in text:
        speak(f"Good evening {name}")


def functionality():
    speak("I can do the following:")
    speak("")
    speak("1.Do a math operation")
    speak("2.Greet you")
    speak("3.Give you the current time")
    speak("4.Give you the current date")
    speak("5.Tell you a joke")
    speak("6.Give you the current weather in your city")


has_set_up = False
name = " "
age = 0
login = input("Type \"yes\" to create a new account or \"no\" to login\n")
if(login.lower()=="yes"):
    with open("file.txt", "rw") as File:
        lines = File.read().splitlines()
        is_val = False
        if len(lines) < 3:
            while True:
                with open("file.txt", "w") as F:
                    age = int(input("What is your age?\n"))
                    speak("Hello and welcome to the personal assistant, I am going to ask you some questions to make my "
                      "performance better than you")
                    try:
                        name = input("What is your name?\n")
                        is_val = True
                    except TypeError:
                        is_val = False
                        speak("Please input your name only")
                    F.write(name)
                    F.write(str(age))
                    lines = F.read().splitlines()
                    name = lines[0]
                    if is_val:
                        break

mat = mat()
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("I am listening")
        r.pause_threshold = .7
        audio = r.listen(source)
    try:
        print("Recognizing")
        Query = r.recognize_google(audio, language = "en-in")
    except Exception as e:
        print(e)
        speak("I did not get that plz repeat yourself")
    return Query
global txt
txt = take_command()
txt = txt.lower()
while txt != "q":
    if txt == "HELP":
        functionality()
    elif "add" in txt or "plus" in txt or "divided" in txt or "multiply" in txt or "times" in txt or "squared" in txt or "square root" in txt or "root" in txt or "minus" in txt or "subtract" in txt or "mod" in txt or "%" in txt or "modulus" in txt:
        mat.nums.clear()
        mat.get_nums(txt)
        list = mat.nums
        string = ""
        for x in range(len(list)):
            string += str(list[x]) + " "
        for x in range(len(list)):
            speak(list[x])
            if list[x].isdigit():
                y = float(list[x])
                list[x] = y


        mat.m_d()

        speak(string + f" = {mat.nums}")

    elif "tell me a joke" in txt.lower() or "give me a joke" in txt or "Tell me a funny joke" in txt:
        response = get("https://official-joke-api.appspot.com/random_ten")

        data = loads(response.text)
        random1 = randint(0, len(data) - 1)
        speak(data[random1]["setup"])
        time.sleep(3)
        speak(data[random1]["punchline"])
        speak(" hahahahahhahaha")

    elif "What is the weather" in txt.lower() or "What is the weather now" in txt  or "What is the current weather oustide" in txt or "weather" in txt:
       txt1 = speak_weather()
       speak(txt1[0])

    elif "miles" in txt and "kilometers" in txt:
        if "convert" in txt or "to" in txt or "in" in txt:
            txt3 = txt.split(" ")
            miles = 0
            for x in range(len(txt3)):
                try:
                    miles = int(txt3[x])
                except:
                    continue
            speak(f"{miles} is {miles*1.609} kilometers")

    elif "time" in txt or "What time is it?" in txt or "What time is right now" in txt:
        now = datetime.now().time()
        hours = now.hour
        mins = now.minute
        text = datetime.today().strftime("%I:%M %p")
        day = ""
        if "AM" in text:
            day = "AM"
        elif "PM" in text:
            day = "PM"
        first_dec = ""
        if mins < 10:
            first_dec = "0"
        speak(f"It is {hours - 12}:{first_dec}{mins} {day}")
    elif "date" in txt or "What is the date?" in txt or "What is today's date" in txt:
        now = str(datetime.today())
        now1 = datetime.today()
        month = ""
        months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
                  9: "September", 10: "October", 11: "November", 12: "December"}
        ending = ""
        nd = [22, 2, 32]
        th = [1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 24, 25, 26, 27, 28, 29, 30, 31]
        rd = [3, 23]
        if now1.day in rd:
            ending = "rd"
        elif now1.day in th:
            ending = "th"
        elif now1.day in nd:
            ending = "nd"
        weekday = now1.weekday()
        weekdays = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
        speak(f"It is {weekdays[weekday]}, {months[now1.month]} {now1.day}{ending}, {now1.year}")
    elif "greet" in txt.lower().strip() or "greet me" in txt.lower().strip():
        greet()
        on_greet = True

    elif txt.upper() == "Q":
        text = datetime.today().strftime("%I:%M %p")
        if "AM" in text:
            speak(f"Have a good morning {name}!")
        elif "PM" in text:
            speak(f"Have a good evening {name}!")
        break
    elif txt != "Q" and txt != "HELP" and on_greet == False and txt != "date":
        speak("Type HELP to see what I can do")
    txt = input("What thing do you want to do or type q to quit and HELP to see what I can do?\n")
