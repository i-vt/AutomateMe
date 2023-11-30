from pynput.mouse import Listener

def on_move(x, y):
    print(f"Mouse moved to ({x}, {y})")

# Create a listener that calls the on_move function when the mouse is moved
with Listener(on_move=on_move) as listener:
    listener.join()
