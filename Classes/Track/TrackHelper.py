import threading

if __name__ != "__main__":
    from .TrackKeyboard import TrackKeyboard as tk
    from .TrackMouse import TrackMouse as tm
    from .TrackScreen import TrackScreen as ts
else:
    from TrackKeyboard import TrackKeyboard as tk
    from TrackMouse import TrackMouse as tm
    from TrackScreen import TrackScreen as ts

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


#TrackHelper().record()
