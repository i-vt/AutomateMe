# Define a combination of classes & functionalities for an easier pull by OchestratorMain.py

import threading, sys, os
if __name__!="__main__":
    from .Track.TrackHelper import TrackHelper as th
else:
    from Track.TrackHelper import TrackHelper as th

class OrchestratorAssistant:
    
    def __init__(self, configs: str = "default"):
        self.configs = configs
        """
        to do: develop new profiles & different configs
        """

    def record(self):
        th().record()

    def play(self, mouse, keyboard):
        if mouse != "":
            mouse_thread = threading.Thread(target=um.play_record(mouse))
            mouse_thread.start()
        if keyboard != "":
            keyboard_thread = threading.thread(target=uk.play_record(keyboard))
            keyboard_thread.start()
        # A bit concerned about delay & file mismatch tbh

#sOrchestratorAssistant().record()
