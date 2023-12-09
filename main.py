#!/usr/bin/env python

import terminal_interaction as ti
import speech_recognition as sr
import os

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        return None 

if __name__ == "__main__":
    while True:
        transcription = recognize_speech()

        if (transcription is not None):
            if (transcription == "clear"):
                os.system("^C") 
            else:
                # Generate zsh command
                zsh_command = f'shell-genie ask "{transcription}"'
                ti.send_to_terminal(zsh_command)
