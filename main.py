import pyttsx3 # text to speech conversion library
import datetime  # for providing date and time
import speech_recognition as sr # for recognizing speech and converting it into text
import wikipedia
import webbrowser
import os
from google import genai  # for integrating gemini 
import requests
from PIL import Image
from io import BytesIO


# for taking voices in window API is provided by windows (sapi 5)

def speak(audio): 
    engine = pyttsx3.init('sapi5') #initialization of the pyttsx3 engine with sapi5
    voices = engine.getProperty('voices') #get the available voices in the system and store it in a variable
    engine.setProperty('voice', voices[1].id) #set engine to use first voice.
    engine.setProperty('rate', 175)
    engine.setProperty('volume', 1)
    engine.say(audio)  #using say method of the engine (queues the audio string to be spoken)
    engine.runAndWait() #processes speech command according to the queue also block all commands untill the queue completed
    engine.stop() #stop the engine after speaking the audio


def wishMe():
    hour = int(datetime.datetime.now().hour) #get the current date and time and extract the hour from it and convert it into integer
    if hour>=0 and hour<12:
        speak("Good Morning sir!")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon sir!")
    else:
        speak("Good Evening sir")

    speak("I am Dash. Please tell me how may I help you")

def takeCommand():  # it takes microphne input from the user and return string output
    r = sr.Recognizer() # recognizer class help us to recognize the audio
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # seconds of non speaking audio before a pharse is consider compleated
        audio = r.listen(source)

    try:
        print("Recognizing...") 
        query = r.recognize_google(audio, language='en-in') # used to convert speech into text
        print(f"You said: {query}\n") 
        return query

    except Exception as e:
        # print (e)

        print("Say that again please....")
        return "None"
    return query

    # takeCommand function is taking audio from the user and converting it into a string 


    #takeComand1 for gemini for taking audio from user



def takeCommand1():  # it takes microphne input from the user and return string output
                    r = sr.Recognizer() # recognizer class help us to recognize the audio
                    with sr.Microphone() as source:
                      print("Listening for gemini...")
                      r.pause_threshold = 1  # seconds of non speaking audio before a pharse is consider compleated
                      audio1 = r.listen(source)

                    try:
                      print("Recognizing...") 
                      query1 = r.recognize_google(audio1, language='en-uk') # used to convert speech into text
                      print(f"You said: {query1}\n") 
                      return query1

                    except Exception as e:
                         # print (e)

                      print("Say that again please....")
                      return "None"
                    return query1
        


def takeCommand2():  # for listening password
                    r = sr.Recognizer() # recognizer class help us to recognize the audio
                    with sr.Microphone() as source:
                      print("Listening for password...")
                      r.pause_threshold = 1  # seconds of non speaking audio before a pharse is consider compleated
                      audio2 = r.listen(source)

                    try:
                      print("Recognizing...") 
                      query2 = r.recognize_google(audio2, language='en-uk') # used to convert speech into text
                      print(f"You said: {query2}\n") 
                      return query2

                    except Exception as e:
                         # print (e)

                      print("Say that again please....")
                      return "None"
                    return query2

def find_folder(folder_name): # to find and open folder in root dir
    """
    Search for a folder in the entire system.

    :param folder_name: The name of the folder to search for.
    :return: A list of paths where the folder is found.
    """
    # Default start directory: Root of the system
    start_directory = "C:\\" if os.name == "nt" else "/"
    found_paths = []
    
    for root, dirs, files in os.walk(start_directory):
        if folder_name in dirs:
            found_paths.append(os.path.join(root, folder_name))
    return found_paths

def takeCommand3():  # for listening folders name which user want to open
                    r = sr.Recognizer() # recognizer class help us to recognize the audio
                    with sr.Microphone() as source:
                      print("Listening for folder name...")
                      r.pause_threshold = 1  # seconds of non speaking audio before a pharse is consider compleated
                      audio3 = r.listen(source)

                    try:
                      print("Recognizing...") 
                      query3 = r.recognize_google(audio3, language='en-uk') # used to convert speech into text
                      print(f"You said: {query3}\n")
                      return query3 

                    except Exception as e:
                         # print (e)

                      print("Say that again please....")
                      return "None"
                    return query3   



if __name__=="__main__":
    speak("Whats your password")
    password = takeCommand2().lower()
    if(password and password =="aditya chauhan 21"):  
      wishMe() 
      while True:
        query = takeCommand().lower()


        while 'gemini' in query:    # for excessing gemini...
            speak("What can I do for you?")
            query1 = takeCommand1().lower()



            api_key = os.getenv("GEMINI_API_KEY")
            if not api_key:
                print("API key not found")
                exit()
            client = genai.Client(api_key=api_key)

            response = client.models.generate_content(
                model="gemini-3-flash-preview",
                contents=query1,
            )
            print(response.text)
            speak(response.text)

            if ('exit' in query1):
                break             

        # for searching somehting on wikipedia

        if 'wikipedia' in query:
            speak("Searching on wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open chat gpt' in query:
            webbrowser.open("chatgpt.com")

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\chauh\\Desktop\\Aditya\\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'tell me the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open vs code' in query:
            codePath = "C:\\Users\\chauh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
            os.startfile(codePath)

        elif 'open riot client' in query:
            rc = "C:\\Riot Games\\Riot Client\\RiotClientServices.exe"
            os.startfile(rc)

        elif 'open chrome' in query:
            gc = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(gc)

        elif 'open folder' in query:   # for acessing and opening the any given folder by the user
            speak("What folder you are looking for")
            query3 = takeCommand3()

            print(f"Searching for '{query3}' from the root directory. This may take a while...\n")
            result = find_folder(query3)
            if result:
             print("Folder found at:")
             for path in result:
              print(path)
              direc = path
              os.startfile(direc)
            else:
              speak("Folder not found!")
            
            


        # image prompt with the help of gemini


        elif 'describe this image' in query:
            api_key = os.getenv("OPENAI_API_KEY")
            client = genai.Client(api_key=api_key)

            print("Enter image URL")

            url = input()
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))

            response = client.models.generate_content(
                model="gemini-1.5-flash",
                contents=["Describe this image in detail", img]
            )
            print(response.text)
            speak(response.text)

        elif 'exit' in query:
            speak("Goodbye sir. Have a nice day!")
            break

    else:
        speak("Wrong Password")



            

            
            