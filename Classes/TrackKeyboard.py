from pynput.keyboard import Listener

def on_keypress(key):
    try:
        # Print the key that was pressed
        print(f'Key pressed: {key.char}')
    except AttributeError:
        # Handle special keys or key combinations
        print(f'Special key pressed: {key}')

# Create a listener that calls the on_keypress function for keyboard events
with Listener(on_press=on_keypress) as listener:
    listener.join()
