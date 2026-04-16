import os
import webbrowser
import datetime

def open_youtube():
    webbrowser.open("youtube.com")

def open_instagram():
    webbrowser.open("instagram.com")

def open_google():
    webbrowser.open("google.com")

def open_chrome():
    os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

def get_time():
    return datetime.datetime.now().strftime("%H:%M:%S")