import os

def send_to_terminal(command):
    os.system(f"xdotool type --delay 30 '{command}'")
    os.system("xdotool key Return")