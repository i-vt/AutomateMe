from pynput.keyboard import Listener, Key

if __name__ != "__main__": from .Track import Track as tk
else: from Track import Track as tk

class TrackKeyboard(tk):
    # To do: add logic for key-press/release for tracking of combination of keys ex.: CTRL + C
    def on_keypress(self, key):
        # print(key)
        self.write_record(self.on_keypress.__name__, key)
        """
        # Not needed here, but probably could be utilized in "UseKeyboard.py"
        try:
            # Check if the key is a special key (like space, enter, etc.)
            if isinstance(key, Key):
                print(f"Special key {key}")
            else:
                # Check if the key is a special character (not a letter or digit)
                if not key.char.isalnum():
                    print(f"Special character {key.char} pressed")
                else:
                    print(f"Alphanumeric key {key.char} pressed")

        except AttributeError:
            print(f"Special key (without char) {key} pressed")
        """
    def record(self):
        # Create a listener that calls the on_keypress function for keyboard events
        with Listener(on_press=self.on_keypress) as listener:
            listener.join()
