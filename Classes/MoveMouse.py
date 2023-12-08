import pyautogui
import time

#To do: Enable read input & act on it, put it into a class

# Move the mouse to a specific location (x, y) on the screen
x, y = 500, 500
pyautogui.moveTo(x, y, duration=1)

# Pause for a moment (optional)
time.sleep(1)

# Perform a right-click
pyautogui.mouseDown(button='right')
pyautogui.mouseUp(button='right')

# Pause for a moment (optional)
time.sleep(1)

# Perform a left-click
pyautogui.mouseDown(button='left')
pyautogui.mouseUp(button='left')
