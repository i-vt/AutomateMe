from pynput.mouse import Listener

def on_move(x, y):
    print(f'Mouse moved to ({x}, {y})')

def on_click(x, y, button, pressed):
    action = "pressed" if pressed else "released"
    print(f'Mouse {action} at ({x}, {y}) with {button}')

def on_scroll(x, y, dx, dy):
    print(f'Scrolled {dx} horizontally and {dy} vertically at ({x}, {y})')

# Create a listener for mouse events
with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    print("Listening for mouse events. Press Ctrl+C to exit.")
    listener.join()
