from pynput.mouse import Listener
import time, Track

class TrackMouse(Track.Track):

    def on_move(self, x, y):
        self.write_record(self.on_move.__name__,x,y)

    def on_click(self, x, y, button, pressed):
        action = "pressed" if pressed else "released"
        self.write_record(self.on_click.__name__, x, y, button, action)

    def on_scroll(self, x, y, dx, dy):
        #Scrolled {dx} horizontally and {dy} vertically with mouse staying at ({x}, {y})
        self.write_record(self.on_scroll.__name__, x, y, dx, dy)


    def record(self):
        # Create a listener for mouse events
        with Listener( on_move=self.on_move, on_click=self.on_click, on_scroll=self.on_scroll) as listener:
            listener.join()
