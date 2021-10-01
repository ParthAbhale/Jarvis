import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import sys
import os
import requests
import json
import pywhatkit as kit
import random
import pyjokes
import pyautogui
import time
from bs4 import BeautifulSoup
from pywikihow import search_wikihow
from pyautogui import click
from keyboard import press
from datetime import date
import calendar
import psutil
import speedtest


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

def speak(audio):
    engine.say(audio)
    print(f"Jarvis: {audio}")
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    min = int(datetime.datetime.now().strftime("%M"))

    if hour > 0 and hour < 12:
        speak('Good Morning Sir')

    elif hour >= 12 and hour < 16:
        speak('Good Afternoon Sir')

    else:
        speak('Good Evening')

    speak('I am Jarvis!Your Computer Asistant')
    curr_date = date.today()
    speak(f"Today is {calendar.day_name[curr_date.weekday()]}")
    if hour > 12:
       hours  = (hour) - 12
    if(hour > 0 and hour < 12):
       speak(f"Its {min} past {hours} AM")
    else:
        speak(f"Its {min} past {hours} PM")




def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.6
        r.energy_threshold = 550
        audio = r.listen(source)
        try:
            print("Recognizing...")
            command = r.recognize_google(audio, language='en-in')
            print(f"User: {command}")

        except Exception as e:
            speak("Sir What did you mean?")
            return "none"
    return command


def getCurrentWeather(cityname):
    apikey = "6648a1a243eb612b204c1e431efad6c8"
    baseUrl = "https://api.openweathermap.org/data/2.5/weather?q="
    cityname = cityname
    completeURL = baseUrl + cityname + "&units=metric" + "&appid=" + apikey
    response = requests.get(completeURL)
    data = response.json()
    temp_of_area = data["main"]["temp"]
    description = data["weather"][0]["description"]
    high_temp = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    speak(f"Current Temperature of our area is { temp_of_area } degree celcius,it looks {description} outside")
    speak(f"Todays maximum temperature will be {high_temp} degree celcius and humidity outside is {humidity}")


def topNews():
    main_url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=1385e142fe3c42f395697e5172e3877f"
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")

def taskExecution():
  work = "false"
  while work != "true":
    query = takeCommand().lower()
    if query != "none":  
        if "wikipedia" in query:
            if "jarvis" in query:
                query  = query.replace("jarvis", "")
            try:
                speak("Searching in Wikipedia...")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak("According to Wikipedia")
                speak(result)
                speak("Anymore Work Sir!")
            except:
                speak("No results found")
                speak("Anymore Work Sir!")
                
        elif "open youtube" in query:
            if "jarvis" in query:
                query  = query.replace("jarvis", "")
            speak("Sir what should play on YouTube")
            speak(f"Playing{query}")
            kit.playonyt(query)
            speak("I finished your work sir anything else.")

        elif "open chrome" in query:
            path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk"
            os.startfile(path)
            query = query.replace("chrome", "")
            speak("I open the chrome sir anything else you want to do you can tell me i will do it for you sir")
        
        elif "are you there" in query:
            speak("Yes Sir,I am there 24 multiplied by 7 for your work!")
            print(query)
            query = query.replace("are u there", "")
            speak("Sir you give some work i will do it for you.")


        elif "what is your name" in query:
            speak("My name is Jarvis!")
            speak("Any work sir")
        
        elif "hey" in query or "hi" in query or "hello" in query:
            speak("hello sir!")
            speak("You can tell me work sir")

        elif "thanks" in query or "thank you" in query:
            speak("No Problem Sir")
            query = query.replace("thanks", "")
            speak("You have any work for me sir")

        elif "who are you" in query:
            query = query.replace("who are you", "")
            speak("I am Jarvis,made by parth,I am a computer program which is made by parth,i am very inteligent you can ask me anything.")
            speak("Want to test my inteligenence")
        
        elif "stop" in query or "abort" in query or "no thanks" in query or "sleep" in query:
            speak("Okay,I am happy that you used me now I am going offline,have great day")
            work = "true"

        elif "how are you" in query:
            speak("I am fine,How are you?")
            query = query.replace("how are you", "")
            cm = takeCommand().lower()
            if "i am" in query and "fine" in cm:
                speak("Okay then its good")
                query = query.replace("i am fine", "")
                speak("So Sir then we shall do Some Work now")
            
        elif "ok" in query:
            speak("Okay fine then tell me sir what should i do for you")

        elif "search" in query:
            if "jarvis" in query:
                query  = query.replace("jarvis", "")
            if "search" in query:
                query = query.replace("search", "")
            try:
                speak("Searching for results...")
                webbrowser.open(f"https://www.google.com/search?q={query}")
                speak("Anymore Work Sir!")
            except:
                speak("No results found")
                speak("Sorry Sir Tell Me Something Else this time i will not disappointe you")

        elif "play" in query:
            if "jarvis" in query:
                query  = query.replace("jarvis", "")
            if "play" in query:
                query = query.replace("play", "")
            try:
                speak(f"Playing{query}")
                kit.playonyt(query)
            except:
                speak("No results found")
                speak("Sorry Sir Tell Me Something Else this time i will not disappointe you")

        elif "send message on whatsapp" in query:
            speak("Tell the phone number sir")
            cm = takeCommand().lower()
            speak("What message should i send sir")
            cm1 = takeCommand().lower()
            hours = int(datetime.datetime.now().hour)
            min = int(datetime.datetime.now().strftime("%M"))
            minutes = min + 2
            kit.sendwhatmsg(f"+91{cm}",cm1,hours,minutes)
            speak("Sending the message sir")
            press('enter')
            speak("Anything else sir")


        elif "open google" in query:
            if "jarvis" in query:
                query  = query.replace("jarvis", "")
            if "search" in query:
                query = query.replace("search", "")
            speak("what should i search on google sir")
            cm = takeCommand().lower()
            webbrowser.open(f"https://www.google.com/search?q={cm}")
            speak("Searching for results...")
            speak("Okay now Any order for me sir")

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            speak("You should now tell me work sir")
        
        elif "speed" in query or "speed test" in query and "check" in query:
            speak("Checking speed sir..")
            speak("Wait a second sir.")
            st = speedtest.Speedtest()
            upload = st.upload()
            download = st.download()
            speak(f"Our Upload speed is{upload} bit per second and our download speed is{download} bit per second.This is the speed report sir...")
            speak("Anything else sir.")

        elif "don't" in query or "properly" in query:
            speak("Okay sir I will try my best to diliver you,For Now tell me anthing else")

        elif "what are you doing" in query:
            speak("I am in your work boss")
        
        elif "mute" in query and "system" in query:
            speak("Ok sir....")
            pyautogui.press('volumemute')
            speak("Sir system volume muted")

        elif "volume up" in query:
            speak("Ok sir....")
            pyautogui.press('volumeup')
            speak("Sir system volume increased")

        elif "volume down" in query:
            speak("Ok sir....")
            pyautogui.press('volumedown')
            speak("Sir system volume decreased")

        elif "mute" in query and "system" in query:
            pyautogui.press('volumemute')
             
        elif "battery" in query and "tell" in query or "what" in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"Sir our system has {percentage} of battery")
            if percentage > 70:
                speak("Sir we have enough energy to work")
            elif percentage > 50 and percentage < 70:
                speak("Sir we have enough energy to work but now you should connect to charger.")
            elif percentage > 30 and percentage < 50:
                speak("Sir we are not having enough energy to work and now you should connect to charger.")
            elif percentage > 10 and percentage < 30:
                speak("Sir we are not having energy at all now you should firstly connect charger.Please sir now you should connect charger or our system will be shutdown.")
            else:
                speak("Sir no energy to work our system will shutdown at anytime please connect to the charger.")


        elif "joke" in query or "jokes" in query:
            jokes  = pyjokes.get_jokes()
            speak("Finding a Good Joke For You")
            speak("Got a Joke")
            speak(jokes)

        elif "restart the system" in query:
            speak("Restarting...")
            os.system("restart /r /t 5")
        
        elif "shutdown the system" in query:
            speak("Doing Process for ShutDown...")
            os.system("shutdown /s /r /t 5")
        
        elif "sleep the system" in query:
            speak("Sleeping...")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        
        elif "story" in query:
            class Person:
                def __init__(self,name, description,moral):
                  self.name = name
                  self.description = description
                  self.moral = moral
            story1 = Person("The Boy Who Cried Wolf","The protagonist of this story is a young shepherd boy living in a village. Every day, the boy would take his flock of sheep to graze on a nearby hill. One day, while the sheep were grazing, the boy felt bored and decided to play a prank on the people of his village. Wolf...Wolf he cried out as loud as he could.Listening to his cries for help, the villagers rushed to help. And, when they came close, he began laughing. When the villagers understood that the boy had fooled them, they were very angry. Warning him not to play the prank again, they returned.However, the boy indulged in the mischief again a few days later. This time too, the villagers warned the boy before returning to the village.A few days later, the villagers heard the boy's cries for help once again. And, this time, it was for real. However, the villagers were tired of being laughed at and didn't think that the boy was really in trouble. So, they ignored his cries for help. And, the wolf killed and ate all his sheep.","People do not believe liars even when they tell the truth. Do not laugh at the  kindness and helpfulness of people, they might not always offer it.")
            story2 = Person("The Midas Touch","There was once a king named Midas who loved gold. One day, God appeared before him and asked him to wish for anything.Being greedy about gold, Midas said, Everything I touch should turn to gold. God granted his wish and told him that, from the nextday, everything he touched would turn to gold.Midas was very happy. He woke up early the next morning and went around touching everything and turning them to gold.After a while, Midas felt hungry. He picked up a piece of bread to eat, but it turned to gold. When hpicked up a glass of water to quench his thirst, it turned to gold as well. As Midas was thinking abouwhat to do, his daughter rushed to him. And, when Midas touched her, she turned into a golden statue.Miserable and teary-eyed, Midas no longer wanted the boon. He prayed to God and atoned for his greed.Pleased by Midas' prayer, God asked him to wash hishands in the nearby river to get rid of the goldentouch.Midas returned after washing his hands and found that everything he had changed to gold had turned back to normal.","People do not believe liars even when they tell the truth. Do not laugh at the  kindness and helpfulness of people, they might not always offer it.")

            story3 = Person("The Camel and the Baby","One day, a baby camel was chatting with her mother. She asked, Mother, why do we have humps, round feet, and long eyelashes Drawing a deep breath, the mother explained, Our humps store water. This helps us survive long journeys in a desert where water is scarce. Our round feet allow us to walk comfortably on sand. And, our long eyelashes protect our eyes from dust and sand, especially during sandstorms.The baby camel remained silent for some time and then asked, Mother, why do we stay in a zoo even when we are blessed with so many qualities?"," Your skills and strengths are of no use if you are not in the right place")

            story4 = Person("The Elephant and Friends","There was once a lonely elephant. One day, he set out to find friends for himself in the jungle. He found a monkey and asked him if he would be a friend. The monkey refused saying, You can't swing from trees like me. The elephant next met a rabbit and asked him to be his friend. The rabbit refused as well saying, You are too big to enter my burrow. The elephant then met a frog, who also refused, saying, You can't leap like me. The elephant ventured deeper into the jungle where he met a fox. The fox also refused the elephant's friendship saying, You are too big.Disheartened, the elephant returned. However, the next day he decided to go to the jungle again. As he entered the jungle, the elephant found all the animals running to save their lives. He stopped the bear to enquire what had happened.The bear said, The tiger wants to eat us and so we are all running to save ourselves.As the elephant was thinking about what he could do to help the animals, the tiger walked up to him.Mr Tiger, please spare these animals. Do not kill and eat them, the elephant implored.Run or I'll kill and eat you as well, growled the tiger.This angered the elephant and he kicked the tiger. The frightened tiger ran away.All the animals now wanted to be friends with the elephant.","You can even be friends with those who are different from you.")

            story5 = Person("The Lion and the Mouse","Once, a mouse accidentally wakes up a lion. This angers the lion and the mouse begs for his life and promises to pay him back in kind. The lion laughs at this but lets the mouse go. A few days later, the mouse finds the lion trapped in a net and sets the lion free by gnawing on the ropes.","No one is too small to help you; everyone has something to offer. And mercy is not a wasted act.")

            story6 = Person("The Wolf and the Shepherd","A hungry wolf came across a farm and tried to eat a sheep. However, the farmers chase him away. The wolf came back after a while and saw some of the farmers enjoying roasted lamb. He thought to himself about how if he had done the same, the farmers would have chased him away and even killed him for having killed an innocent lamb.","We judge other people for actions that we don't judge ourselves for doing.")

            all_stories = [story1,story2,story3,story4,story5,story6]
            story = random.choice(all_stories)
            speak(f"The name of the story is {story.name}")
            speak(story.description)
            speak(f"The moral of the story is {story.moral}")

        elif "switch" in query or "change" in query and "screen" in query :
            speak("Switching to the next window sir")
            pyautogui.keyDown("alt")
            pyautogui.keyDown("tab")
            pyautogui.keyUp("alt")
            speak("Changed the window sir!Anything more for me")

        elif "where we are" in query or "where do we live" in query:
            speak("Sir we live in shirdi")
            speak("And in shirdi we live in govindnagar")

        elif "today's news" in query:
            speak("Fetching todays news for you sir")
            topNews()
            speak("I am ready sir you can tell work to me now")

        elif "take" in query and "screenshot" in query:
           speak("Please hold the screen for a second sir i am taking screenshot")
           time.sleep(3)
           img = pyautogui.screenshot() 
           speak("Sir I Took the screenshot now tell me the name for the screenshot image to save")
           name = takeCommand().lower()
           img.save(f"{name}.png")
           speak("Sir I am done Saved the screenshot in our folder")
           speak("Anything else sir")
        
        elif "do calculations" in query:
            speak("Which kind of operations you have to do sir tell me the operater")
            operater = input("Enter the operater: ")
            speak("Okay now sir tell me the first value")
            num1 = input("Enter the first number: ")
            number1 = int(num1)
            speak("Okay,Okay now sir tell me the second value")
            num2 = input("Enter the second number: ")
            number2 = int(num2)
            if "plus" in operater or "+" in operater:
                results = number1 + number2
                speak(f"The answer of the given problem is: {results}")
            elif "minus" in operater or "-" in operater:
                results = number1 - number2
                speak(f"The answer of the given problem is: {results}")
            elif "divide" in operater or "division" in operater:
                results = number1 / number2
                speak(f"The answer of the given problem is: {results}")
            elif "times" in operater or "multiply" in operater:
                results = number1 * number2
                speak(f"The answer of the given problem is: {results}")

            else:
                speak("Invalid operator!")
                speak("Sorry Sir Tell Me Something Else this time i will not disappointe you")
            
        elif "weather" in query and "forecast" in query:
                speak("Which city's weather forecast you want sir")
                search = takeCommand().lower()
                wether = f"weather of {search}"
                url = f"https://www.google.com/search?q={wether}"
                r = requests.get(url)
                data  = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div",class_= "BNeawe").text
                speak(f"current {search} is {temp}")

        elif "activate how to do mod" in query:
            if "jarvis" in query:
                query = query.replace("jarvis","")
            speak("How to do mod activated sir")
            while True:
                  speak("What you have to search sir")
                  how = takeCommand().lower()
                  if "exit how to do mod" in how or "close how to do mod" in how:
                    speak("How to do mod disactivated")
                    break
                  else:  
                         max_results = 1
                         how_to = search_wikihow(how,max_results)
                         assert len(how_to) == 1
                         how_to[0].print()
        elif "i am getting bor" in query or "i am getting bored" in query or "i am bored" in query:
            speak("Sir should I play music")
            cm = takeCommand().lower()
            if "yes" in cm:
                speak("Sir which music should I play for you")
                if "jarvis" in query:
                 query  = query.replace("jarvis", "")
                if "search" in query or "play" in query:
                    query = query.replace("search", "")
                    query = query.replace("play", "")
                music = takeCommand().lower()
                kit.playonyt(music)

            if "no" in cm:
                speak("Then what should I do for you sir")
            
        

                    
        elif query != "none":
            if "jarvis" in query:
                query  = query.replace("jarvis", "")
            webbrowser.open(f"https://www.google.com/search?q={query}")


    else:
       speak("Sir can you repeat")

if __name__ == '__main__':
  if 1:
        wishMe()
        getCurrentWeather("shirdi")
        speak("How May I help you Sir")
        taskExecution()
  while True:
    query = input("Should Jarvis Wake up: ")
    if "wake up" in query:
        speak("Yes Sir I am Ready To do Work, Jarvis Status Online...")
        taskExecution()
    elif "goodbye" in query:
        speak("Yes Good bye sir")
        sys.exit()