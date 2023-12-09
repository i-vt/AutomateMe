import os, Track, time
from PIL import ImageGrab

#Remove dependency if single screen?
from screeninfo import get_monitors

class TrackScreen(Track.Track):

    def capture_screens(self,folder_path, naming: str="screenshot"):
        for i, m in enumerate(get_monitors()):
            # The bounding box is defined by the geometry of the monitor
            bbox = (m.x, m.y, m.x + m.width, m.y + m.height)
            print(f"Capturing screen {m.name} at bbox: {bbox}")
            screenshot = ImageGrab.grab(bbox=bbox)
            screenshot_path = os.path.join(folder_path, f'{naming}_{i + 1}_{self.now()}.png')
            screenshot.save(screenshot_path)
        return True


    def record(self,iterations: int = -1, 
                    sleep_time: float=0.5, 
                    folder_name: str="Screenshots",
                    file_naming: str="screenshot"):
        output_folder = self.make_local_folder_get_filepath(folder_name)

        while iterations != 0:
            print(output_folder)
            self.capture_screens(output_folder, file_naming)
            time.sleep(sleep_time)
            iterations -= 1

