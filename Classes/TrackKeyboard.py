from pynput.keyboard import Key, Listener

def on_press(key):
    try:
        # Check if the key is a special key (like space, enter, etc.)
        if isinstance(key, Key):
            print(f"Special key {key} pressed")
        else:
            # Check if the key is a special character (not a letter or digit)
            if not key.char.isalnum():
                print(f"Special character {key.char} pressed")
            else:
                print(f"Alphanumeric key {key.char} pressed")

    except AttributeError:
        print(f"Special key (without char) {key} pressed")

def on_release(key):
    # Stop listener
    if key == Key.esc:
        return False

# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
