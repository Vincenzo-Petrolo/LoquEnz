#!/usr/bin/env python

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
        return "Could not understand audio"
    except sr.RequestError as e:
        return f"Error with the speech recognition service: {e}"

if __name__ == "__main__":
    while True:
        input("Press Enter to start recognition...")
        transcription = recognize_speech()
        
        # Generate zsh command
        zsh_command = f'shell-genie ask "{transcription}"'
        
        # Execute the zsh command
        os.system(zsh_command)
