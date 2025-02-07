import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import random
import subprocess

listener = sr.Recognizer()
engine = pyttsx3.init()

# Configure voice settings
voices = engine.getProperty('voices')
if len(voices) > 1:
    engine.setProperty('voice', voices[1].id)  # Female voice
else:
    engine.setProperty('voice', voices[0].id)  # Fallback to default
engine.setProperty('rate', 150)  # Adjust speech rate


def talk(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        listener.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = listener.listen(source, timeout=5, phrase_time_limit=8)
            command = listener.recognize_google(audio).lower()
            print(f"Raw input: {command}")
            if 'jarvis' in command:
                return command.split('jarvis', 1)[1].strip()
            return ''
        except sr.WaitTimeoutError:
            print("No speech detected.")
            return ''
        except sr.UnknownValueError:
            print("Could not understand audio.")
            return ''
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return ''


def open_program(program_name):
    apps = {
        'chrome': 'start chrome',
        'notepad': 'notepad',
        'calculator': 'calc',
        'spotify': 'spotify',
        'word': 'winword',
        'excel': 'excel'
    }

    program_name = program_name.lower()
    for key, cmd in apps.items():
        if key in program_name:
            talk(f"Opening {key}")
            os.system(cmd)
            return
    talk(f"Sorry, I don't know how to open {program_name}")


def search_web(query):
    talk(f"Searching for {query}")
    webbrowser.open(f"https://www.google.com/search?q={query}")


def play_song(song_name):
    talk(f"Playing {song_name}")
    webbrowser.open(f"https://www.youtube.com/results?search_query={song_name.replace(' ', '+')}")


def tell_joke():
    jokes = [
        "Why don't skeletons fight each other? They don't have the guts.",
        "What do you call a fish wearing a bowtie? Sofishticated.",
        "Why did the math book look sad? Because it had too many problems."
    ]
    talk(random.choice(jokes))


def run_jarvis():
    talk("Initializing Jarvis. How can I assist you today?")
    
    while True:
        command = listen()
        if not command:
            continue

        print(f"Command received: {command}")
        parts = command.split(maxsplit=1)
        primary = parts[0].lower()
        secondary = parts[1] if len(parts) > 1 else None

        if 'time' in command:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            talk(f"The current time is {current_time}")
        elif primary == 'hello':
            talk('Hello there! How can I help you?')
        elif primary == 'open':
            if secondary:
                open_program(secondary)
            else:
                talk("Please specify what to open")
        elif primary == 'search':
            if secondary:
                search_web(secondary)
            else:
                talk("Please specify your search query")
        elif primary == 'play':
            if secondary:
                play_song(secondary)
            else:
                talk("Please specify what to play")
        elif primary == 'joke':
            tell_joke()
        elif 'date' in command:
            current_date = datetime.datetime.now().strftime('%B %d, %Y')
            talk(f"Today's date is {current_date}")
        elif primary in ['exit', 'quit', 'bye']:
            talk("Goodbye! Have a wonderful day.")
            break
        elif primary == 'help':
            help_text = "I can: Tell time/date, open apps (Chrome, Notepad, etc), "
            help_text += "search the web, play videos, tell jokes, and more!"
            talk(help_text)
        else:
            talk("I didn't understand that. Please try again or say 'help' for options.")


if __name__ == "__main__":
    run_jarvis()