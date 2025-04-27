import eel
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pywhatkit as kit
import pyjokes
import pyautogui
import os
import webbrowser

# Importing WhatsApp feature
from feature import send_WhatsApp_message

# Initialize Eel with frontend folder
eel.init("web")

# Initialize TTS engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis, Please tell me how may I help you Sir")
    eel.updateStatus("I am Jarvis, ready to help you!")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        eel.updateStatus("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        eel.updateStatus("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        eel.updateStatus(f"You said: {query}")
    except Exception:
        print("Say that again please...")
        eel.updateStatus("Couldn't recognize. Please say again.")
        return "None"
    return query.lower()

def tellTime():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The time is {time}")
    eel.updateStatus(f"Time is {time}")

def openApplication(query):
    query = query.lower()
    if 'chrome' in query:
        speak("Opening Google Chrome")
        os.system("start chrome")
    elif 'firefox' in query:
        speak("Opening Mozilla Firefox")
        os.system("start firefox")
    elif 'notepad' in query:
        speak("Opening Notepad")
        os.system("start notepad")
    elif 'word' in query or 'microsoft word' in query:
        speak("Opening Microsoft Word")
        os.system("start winword")
    elif 'powerpoint' in query:
        speak("Opening PowerPoint")
        os.system("start powerpnt")
    elif 'excel' in query:
        speak("Opening Excel")
        os.system("start excel")
    elif 'youtube' in query:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif 'whatsapp' in query:
        speak("Opening WhatsApp")
        webbrowser.open("https://web.whatsapp.com")
    elif 'calendar' in query:
        speak("Opening Calendar")
        os.system("start outlookcal:")
    elif 'calculator' in query:
        speak("Opening Calculator")
        os.system("start calc")
    else:
        speak("Application not recognized.")
        eel.updateStatus("App not recognized.")

def searchWikipedia(query):
    speak("Searching Wikipedia...")
    query = query.replace("wikipedia", "")
    try:
        results = wikipedia.summary(query, sentences=1)
        speak("According to Wikipedia:")
        print(results)
        speak(results)
        eel.updateStatus(results)
    except wikipedia.exceptions.DisambiguationError:
        speak("Multiple results found. Please be more specific.")
        eel.updateStatus("Multiple results found.")
    except wikipedia.exceptions.PageError:
        speak("No page found.")
        eel.updateStatus("Wikipedia page not found.")

def tellJoke():
    joke = pyjokes.get_joke()
    speak(joke)
    eel.updateStatus(joke)

def searchWeb(query):
    speak("Searching the web")
    kit.search(query)
    eel.updateStatus("Searching: " + query)

def takeScreenshot():
    speak("Taking a screenshot")
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    speak("Screenshot saved as screenshot.png")
    eel.updateStatus("Screenshot saved")

def openYouTube(query):
    query = query.replace("play", "")
    speak(f"Playing {query} on YouTube")
    kit.playonyt(query)
    eel.updateStatus(f"Playing {query} on YouTube")

def closeApp(query):
    query = query.lower()
    if 'chrome' in query:
        speak("Closing Google Chrome")
        os.system("taskkill /f /im chrome.exe")
    elif 'firefox' in query:
        speak("Closing Mozilla Firefox")
        os.system("taskkill /f /im firefox.exe")
    elif 'notepad' in query:
        speak("Closing Notepad")
        os.system("taskkill /f /im notepad.exe")
    elif 'word' in query or 'microsoft word' in query:
        speak("Closing Microsoft Word")
        os.system("taskkill /f /im winword.exe")
    elif 'powerpoint' in query:
        speak("Closing PowerPoint")
        os.system("taskkill /f /im powerpnt.exe")
    elif 'excel' in query:
        speak("Closing Excel")
        os.system("taskkill /f /im excel.exe")
    elif 'whatsapp' in query:
        speak("Closing WhatsApp")
        os.system("taskkill /f /im whatsapp.exe")
    elif 'calendar' in query:
        speak("Closing Calendar")
        os.system("taskkill /f /im outlook.exe")
    elif 'calculator' in query:
        speak("Closing Calculator")
        os.system("taskkill /f /im calc.exe")
    else:
        speak("Application not recognized or not running")
        eel.updateStatus("App not recognized or not running.")

@eel.expose
def start_jarvis():
    wishMe()
    while True:
        query = takeCommand()

        if "time" in query:
            tellTime()
        elif "wikipedia" in query:
            searchWikipedia(query)
        elif "joke" in query:
            tellJoke()
        elif "open" in query:
            openApplication(query)
        elif "search" in query:
            searchWeb(query)
        elif "screenshot" in query:
            takeScreenshot()
        elif "youtube" in query or "play" in query:
            openYouTube(query)
        elif "close" in query:
            closeApp(query)
        elif "send whatsapp message" in query:
            try:
                speak("To whom do you want to send the message?")
                eel.updateStatus("Listening for contact name...")
                name = takeCommand()

                speak("What message do you want to send?")
                eel.updateStatus("Listening for message...")
                message = takeCommand()

                send_WhatsApp_message(name, message)

            except Exception as e:
                print(f"Error while sending WhatsApp message: {e}")
                speak("Sorry, I couldn't send the WhatsApp message.")
                eel.updateStatus("Failed to send WhatsApp message.")
        elif "exit" in query or "quit" in query or "bye" in query:
            speak("Goodbye Sir, have a nice day!")
            eel.updateStatus("Jarvis closed.")
            break

# Launch the app
eel.start("index.html", size=(700, 500))
