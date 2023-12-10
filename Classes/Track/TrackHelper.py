# Define a combination of classes & functionalities for an easier pull by OchestratorMain.py

from .TrackKeyboard import TrackKeyboard as tk
from .TrackMouse import TrackMouse as tm
from .TrackScreen import TrackScreen as ts
import threading

class TrackHelper:
    
    def __init__(self, configs: str = "default"):
        self.configs = configs
        """
        to do: develop new profiles & different configs
        """
    def mouse(self):tm().record()
    def keyboard(self):tk().record()
    def screen(self):ts().record()

    def record(self):
        #Easier to do it this way so they do not self-initiate lol b/c of multiple parenthesis
        screen_screen = threading.Thread(target=self.screen)
        mouse_thread = threading.Thread(target=self.mouse)
        keyboard_thread = threading.Thread(target=self.keyboard)
        
        screen_screen.start()
        mouse_thread.start()
        keyboard_thread.start()

        """
        #keyboard = threading.Thread(target=tk().record())
        screen  = threading.Thread(target=ts().record())
        print(1)
        screen.start()
        print(2)
        mouse.start()
        print(3)
        #keyboard.start()
        screen.join()
        mouse.join()
        #keyboard.join()
        """

#TrackHelper().record()
