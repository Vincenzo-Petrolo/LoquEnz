#!/usr/bin/env python

import terminal_interaction as ti

import time

import speech_recognition as sr

def callback(recognizer : sr.Recognizer, audio):
    # received audio data, now we'll recognize it using Google Speech Recognition
    try:
        transcript = recognizer.recognize_google(audio)
        print(transcript)
        if (transcript == "clear"):
            ti.send_to_terminal("\x03")
        else:
            ti.send_to_terminal(f'shell-genie ask "{transcript}"')
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening

# start listening in the background (note that we don't have to do this inside a `with` statement)
stop_listening = r.listen_in_background(m, callback)
# `stop_listening` is now a function that, when called, stops background listening

# do some unrelated computations for 5 seconds
while(1):
    print("LoquEnz is running")
    time.sleep(20)  # we're still listening even though the main thread is doing other things