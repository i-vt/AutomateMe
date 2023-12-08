# To do: create a class, add a method for saving, and continuous sequential screenshots.
from PIL import ImageGrab
from screeninfo import get_monitors

def capture_screens():
    screenshots = []
    for m in get_monitors():
        # The bounding box is defined by the geometry of the monitor
        bbox = (m.x, m.y, m.x + m.width, m.y + m.height)
        print(f"Capturing screen {m.name} at bbox: {bbox}")
        screenshot = ImageGrab.grab(bbox=bbox)
        screenshots.append(screenshot)

    return screenshots

# Capture all screens
all_screenshots = capture_screens()

# Optionally, save each screenshot
for i, screenshot in enumerate(all_screenshots):
    screenshot.save(f"screen_{i+1}.png")
