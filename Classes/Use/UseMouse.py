import time
from pynput.mouse import Button, Controller

if __name__ != "__main__": from .Use import Use
else: from Use import Use

class UseMouse(Use):

    def play_record(self, instruction_file: str="", delimiter: str="|") -> bool:
        """
        filepath = "/home/computer/Documents//Output/TrackMouse_20231209_141013_599845.txt"
        UseMouse().play_record(filepath)
        
        returns true if completed without issues, false if failed.
        """
        if instruction_file == "": return False
        valid_list = self.read_file(instruction_file, delimiter)
        mouse = Controller()
        for command in valid_list:
            time.sleep(command[0])
            print(command)
            if command[1] == "on_move":
                mouse.position = (int(command[2]),int(command[3]))

            elif command[1] == "on_click":
                mouse.position = (int(command[2]), int(command[3]))

                if command[4] == "Button.left" and command[5] == "pressed":
                    mouse.press(Button.left)

                elif command[4] == "Button.right" and command[5] == "pressed":
                    mouse.press(Button.right)

                elif command[4] == "Button.left" and command[5] == "released":
                    mouse.release(Button.left)

                elif command[4] == "Button.right" and command[5] == "released":
                    mouse.release(Button.right)


            elif command[1] == "on_scroll":
                mouse.position = (int(command[2]), int(command[3]))
                mouse.scroll(int(command[4]), int(command[4]))

            else: continue
        return True
