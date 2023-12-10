from pynput.keyboard import Controller, Key
import time, random

if __name__ != "__main__": from .Use import Use as u
else: from Use import Use as u

class UseKeyboard(u):
    def __init__(self,timing: str="random", variance: float=.25):
        """
            TIMING
        random: Generated randomly between 0.625 and 0.475 to average .5 per character or 120 wpm
        custom_predefined: Custom per character / key-press
        custom_randomized: Custom range, but randomized per char/key-press
        """
        allowed_timing = ["random", "custom_predefined", "custom_randomized"]
        if timing not in allowed_timing: raise ValueError
        self.keyboard = Controller()
        self.timing = timing
        self.variance = variance

        self.CONST_TIMING = 0.5


    def type_char(self, passed_character: str="", wait_time: float=0.1) -> bool:
        time.sleep(wait_time)
        try:
            self.keyboard.type(passed_character)
        except ex as Exception:
            print(ex)
            return False
        return True

    def type_basic(self, word, custom_timing) -> bool:
        """
        Used for basic characters (not special characters ex.: <alt>)
        """
        word = str(word)

        if "custom" in self.timing: 
            if "predefined" in self.timing:
                if len(word) != len(custom_timing): return False
                for key in range(len(word)): 
                    if self.type_char(word[key], custom_timing[key]) != True: return False
                return True

            #Fix the logic here, move this to the random &  optimize
            else:
                length = len(str(custom_timing))
                interval_top = int(custom_timing*length*(1+self.variance))
                interval_bottom = int(custom_timing*length*(1-self.variance))
                
                for key in range(len(word)):
                    self.type_char(word[key], random.randint(interval_bottom, interval_top)/length)
                return True
        else:
            custom_timing = self.CONST_TIMING
            length = len(str(custom_timing))
            interval_top = int(custom_timing*length*(1+self.variance))
            interval_bottom = int(custom_timing*length*(1-self.variance))
                
            for key in range(len(word)):
                
                self.type_char(word[key], random.randint(interval_bottom, interval_top)/length)
            return True
        return False
    def click_release(self, special_key):
        # Only for special keys such as ctrl,shift,cmd(aka winkey), caps
        self.keyboard.press(special_key)
        self.keyboard.release(special_key)

    def play_record(self, instruction_file: str="", delimiter: str = "|") -> bool:
        """
        filepath = "/home/computer/Documents//Output/TrackKeyboard_20231209_141013_599845.txt"
        UseKeyboard().play_record(filepath)
        
        returns true if completed without issues, false if failed.
        """
        if instruction_file == "": return False
        valid_list = self.read_file(instruction_file, delimiter)
        print("bow!")
        for command in valid_list:
            time.sleep(command[0])
            print(command)
            if command[1] == "on_keypress":
                if "'" in command[2] or '"' in command[2] : 
                    command[2] = command[2][1:-1] 
                    self.click_release(command[2])
                elif "Key.ctrl" == command[2]:
                    self.click_release(Key.ctrl)
                elif "Key.shift" == command[2]:
                    self.click_release(Key.shift)
                elif "Key.caps_lock" == command[2]:
                    self.click_release(Key.caps_lock)
                elif "Key.cmd" == command[2]:
                    self.click_release(Key.cmd)
                elif "Key.esc" == command[2]:
                    self.click_release(Key.esc)
            else: continue

        return True


