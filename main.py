# Press the green button in the gutter to run the script.
import speech_recognition as aa
import pyttsx3   #pyttsx3 is a text-to-speech conversion library in Python
#from translate import Translator
import pywhatkit #it is one of the most popular library for WhatsApp and YouTube automation.
import datetime
import wikipedia
import openai
import os
import pandas as pd


listener = aa.Recognizer()
#All of the magic in SpeechRecognition happens with the Recognizer class.
#The primary purpose of a Recognizer instance is, of course, to recognize speech.
# Each instance comes with a variety of settings and functionality for recognizing speech from an audio source.
machine = pyttsx3.init()
#an application uses the engine object to register and unregister event callbacks; produce and stop speech; get
# and set speech engine properties; and start and stop event loops.
#eng = pyttsx3.init()
voice = machine.getProperty('voices')

openai.api_key = "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"

def talk(text):
    machine.setProperty('voice', voice[1].id)
    machine.say(text)
    #takes a string value and speaks it out. This function keeps track when the engine starts converting text to
    # speech and waits for that much time, and do not allow the engine to close
    machine.runAndWait()
    # to start the engine and block the application until the engine has finished speaking both phrases.

def input_instruction():
    global instruction
    try:
        with aa.Microphone() as origin: #Creates a new Microphone instance, which represents a physical microphone on the computer.
            print("listening...")
            speech = listener.listen(origin) #Records a single phrase from source (an AudioSource instance) into an AudioData instance, which it returns.
            instruction = listener.recognize_google(speech,language="en-in")
            instruction = instruction.lower()
            if "Jarvis" in instruction:
                instruction = instruction.replace('Jarvis'," ")
                print(instruction)



    except:
        pass
    return instruction

def get_chatgpt_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()


def play_Jarvis():

    instruction = input_instruction()
    print(instruction)
    if "play" in instruction:
        song = instruction.replace('Jarvis play', "")
        talk("Playing " + song)
        print("Playing" + song)
        pywhatkit.playonyt(song)

    elif 'search google' in instruction:
        word = instruction.split('about')
        wordy=word[1]
      #  word = instruction.replace('Jarvis search',"about")
        pywhatkit.search(wordy)

    elif 'open google' in instruction:
        words = instruction.split('google')
        worde = words[1]
        pywhatkit.search(worde)

    elif 'time' in instruction:
        time = datetime.datetime.now().strftime('%I:%M%p')
        talk('current time'+ time)
        print('Current Time : '+ time)

    elif 'date' in instruction:
        date = datetime.datetime.now().strftime('%d /%m /%Y')
        talk("Today's date is"+ date)
        print("Today's date: "+ date)

    elif 'how are you' in instruction:
        talk('I am fine, how about you?')
        print('I am fine, how about you?')

    elif 'what is your name' in instruction:
        talk("What's in a name? Although, I am Jarvis. What can I do for you?")
        print("What's in a name? Although, I am Jarvis. What can I do for you?")

    elif 'chat' in instruction:  # New elif statement for chat
        chat_prompt = instruction.replace('Jarvis ask chat', "").strip()
        chatgpt_response = get_chatgpt_response(chat_prompt)
        talk(chatgpt_response)
        print("ChatGPT:", chatgpt_response)

    elif "using wikipedia search".lower() in instruction:
        find = instruction.split("using wikipedia search")
        finder = find[1]
        talk("Information displayed:")
        print(wikipedia.page(finder, 1).content)

    else:
        talk("Please repeat")

play_Jarvis()

