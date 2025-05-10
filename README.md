# Python Keylogger - Keystroke and Window Tracker

This simple Python project demonstrates how to build a simple keylogger that tracks keystrokes and records the active window in real-time. The keylogger logs each key pressed and tracks the currently focused window, saving all information into a log file with timestamps.

## Features
- Capture keystrokes in real-time.
- Track and log the active window title.
- Compatible with both **Windows** and **Linux** systems.
- Logs data into a `log.txt` file for later review.

## Prerequisites

This project assumes the required libraries are already installed. If not, make sure to install them beforehand:

- **`pynput`**: For capturing keyboard events.
- **`pywin32`**: For Windows users to interact with system GUI.
- **`xdotool`**: For Linux users to capture window titles (make sure it's installed if you're on Linux).

If you don't have these libraries installed, you can install them using the following commands:

```bash
pip install pynput pywin32
```

