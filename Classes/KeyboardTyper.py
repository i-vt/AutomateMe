from pynput.keyboard import Controller
import time, random

# To do: enable easier handling of special keys
# You can also simulate keypresses, for example, pressing and releasing the 'Enter' key:
# keyboard = Controller()
# keyboard.press(Key.enter)
# keyboard.release(Key.enter)


class KeyboardTyper:
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



"""
#Testing
if __name__ == "__main__":
    KeyboardTyper().type_basic("AAAaaaaAbd*", 10)
"""
