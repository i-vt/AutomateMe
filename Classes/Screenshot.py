import os
import platform
from PIL import ImageGrab

# To do: create a class, add a method for saving, and continuous sequential screenshots.

def capture_screens():
    # Get the number of screens
    num_screens = len(ImageGrab.grab_all())

    # Create a directory to store the screenshots
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')

    for screen_idx in range(num_screens):
        # Capture the screenshot of the current screen
        screenshot = ImageGrab.grab(all_screens=True, screen=screen_idx)

        # Save the screenshot to a file
        filename = f'screenshot_{screen_idx + 1}.png'
        screenshot.save(os.path.join('screenshots', filename))
        print(f'Screenshot {screen_idx + 1} saved as {filename}')

if __name__ == '__main__':
    capture_screens()
