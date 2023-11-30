from pynput.keyboard import Controller
import time

keyboard = Controller()

# Type the text
text_to_type = "Hello, World!"
for char in text_to_type:
    keyboard.type(char)
    time.sleep(0.1)  # Add a small delay between each character

# You can also simulate keypresses, for example, pressing and releasing the 'Enter' key:
# keyboard.press(Key.enter)
# keyboard.release(Key.enter)
