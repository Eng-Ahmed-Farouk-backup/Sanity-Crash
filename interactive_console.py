import os
import time
import keyboard

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def interactive_menu(options, header = ""):
    current = 0
    clear_console()
    print(header)
    for i,option in enumerate(options):
        print(f"-> {option}" if i == current else f"   {option}")
    time.sleep(1)
    while True:
        clear_console()
        print(header)
        for i,option in enumerate(options):
            print(f"-> {option}" if i == current else f"   {option}")
        
        key = keyboard.read_key()
        if key == "up" or key == "down":
            current = (current + 1)%len(options) if key == "down" else (current - 1)%len(options)
        elif key == "enter":
            return options[current]
        


def println(msg):
    for m in msg.split("\n"):
        print(m)
        start_time = time.time()
        while time.time() < start_time+max(len(m)/25,3):
            key = keyboard.is_pressed("space")
            if key:break
        time.sleep(0.2)
