# Define a combination of classes & functionalities for an easier pull by OchestratorMain.py

import Track.TrackKeyboard as tk, Track.TrackMouse as tm, Track.TrackScreen as ts
import Use.UseKeyboard as uk, Use.UseMouse as um

import threading

class OrchestratorAssistant:
    
    def __init__(self, configs: str = "default"):
        self.configs = configs
        """
        to do: develop new profiles & different configs
        """

    def record(self):
        keyboard =  = threading.thread(target=tk().record())
        mouse  = threading.thread(target=tm().record())
        screen  = threading.thread(target=ts().record())
        
        screen.start()
        mouse.start()
        keyboard.start()

    def play(self, mouse, keyboard):
        if mouse != "":
            mouse_thread = threading.Thread(target=um.play_record(mouse))
            mouse_thread.start()
        if keyboard != "":
            keyboard_thread = threading.thread(target=uk.play_record(keyboard))
            keyboard_thread.start()
        # A bit concerned about delay & file mismatch tbh
