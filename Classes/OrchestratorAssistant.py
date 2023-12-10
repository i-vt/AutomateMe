# Define a combination of classes & functionalities for an easier pull by OchestratorMain.py

import threading, sys, os
if __name__!="__main__":
    from .Track.TrackHelper import TrackHelper as th
    from .Use.UseHelper import UseHelper as uh
else:
    from Track.TrackHelper import TrackHelper as th
    from Use.UseHelper import UseHelper as uh

class OrchestratorAssistant:
    
    def __init__(self, configs: str = "default"):
        self.configs = configs
        """
        to do: develop new profiles & different configs
        """

    def record(self):
        th().record()

    def play(self, mouse, keyboard):
        """
        m = "/home/computer/Downloads/Samples/TrackMouse_20231210_001637_845342.txt"
        k = "/home/computer/Downloads/Samples/TrackKeyboard_20231210_001637_846024.txt"
        OrchestratorAssistant().play(m,k)
        """
        uh().play_record(mouse,keyboard)
