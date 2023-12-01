from pynput.mouse import Listener
import time, datetime, os, inspect

class TrackMouse:
    def __init__(self, output_option: str = "default", output_folder: str = "", delim: str = "|"):
        """
        Valid output_option choices:
        - default: outpout to ./Output/Mouse_YYYYMMDD_hhmmss.txt; argument: none
        - custom: pick a new path, but pick using args
        - SQL: configs for an integration
        """
        valid_output_options = ["default", "custom"]
        if output_option not in valid_output_options:  raise ValueError
        if output_folder == "": 
            script_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
            output_folder = os.path.join(script_dir, "Output/")
        
        self.output_option = output_option
        self.output_folder = output_folder

        now = datetime.datetime.now()
        output_file = now.strftime("Mouse_%Y%m%d_%H%M%S_%f.txt")

        if not os.path.exists(output_folder): os.makedirs(output_folder)

        self.output_path = os.path.join(output_folder, output_file)

        self.delim = delim


    def write(self, text):
        """
        assuming default self.delim  "|"
        function|args1|agrs2|...|argsn
        """
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y%m%d_%H%M%S_%f")
        with open(self.output_path, "a") as file: file.write(timestamp + self.delim + text+"\n")

    def on_move(self, x, y):
        self.write(f"on_move{self.delim}{x}{self.delim}{y}")

    def on_click(self, x, y, button, pressed):
        action = "pressed" if pressed else "released"
        self.write(f"on_click{self.delim}{x}{self.delim}{y}{self.delim}{button}{self.delim}{action}")

    def on_scroll(self, x, y, dx, dy):
        #Scrolled {dx} horizontally and {dy} vertically with mouse staying at ({x}, {y})
        self.write(f"on_scroll{self.delim}{x}{self.delim}{y}{self.delim}{dx}{self.delim}{dy}")


    def record(self):
        # Create a listener for mouse events
        with Listener( on_move=self.on_move, on_click=self.on_click, on_scroll=self.on_scroll) as listener:
            listener.join()



 
# Test
# TrackMouse().record()
