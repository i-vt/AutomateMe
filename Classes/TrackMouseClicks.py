from pynput.mouse import Listener

def on_click(x, y, button, pressed):
    if pressed:
        if button == button.left:
            print(f"Left mouse button clicked at ({x}, {y})")
        elif button == button.right:
            print(f"Right mouse button clicked at ({x}, {y})")

# Create a listener that calls the on_click function for mouse clicks
with Listener(on_click=on_click) as listener:
    listener.join()
