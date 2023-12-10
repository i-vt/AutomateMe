import threading

if __name__ != "__main__":
    from .UseKeyboard import UseKeyboard as uk
    from .UseMouse import UseMouse as um
else:
    from UseKeyboard import UseKeyboard as uk
    from UseMouse import UseMouse as um


class UseHelper:
    
    def __init__(self, configs: str = "default"):
        self.configs = configs
        """
        to do: develop new profiles & different configs
        """
    def mouse(self):um().play_record(self.mouse_instruction_filepath)
    def keyboard(self):uk().play_record(self.keyboard_instruction_filepath)

    def play_record(self, mouse_instruction_filepath: str="", keyboard_instruction_filepath: str=""):
        """
        mouse = "/home/computer/Documents/TrackMouse_20231209_233404_684467.txt"
        keyboard = "/home/computer/Documents/TrackKeyboard_20231209_233404_684467.txt"
        UseHelper().play_record(mouse,keyboard)
        replays the recorded instructions
        """
        
 
        #Easier to do it this way so they do not self-initiate lol b/c of multiple parenthesis
        if mouse_instruction_filepath != "":
            self.mouse_instruction_filepath = mouse_instruction_filepath
            mouse_thread = threading.Thread(target=self.mouse)
            mouse_thread.start()

        if keyboard_instruction_filepath != "":
            self.keyboard_instruction_filepath = keyboard_instruction_filepath
            keyboard_thread = threading.Thread(target=self.keyboard)
            keyboard_thread.start()
