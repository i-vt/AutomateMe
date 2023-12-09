from datetime import datetime
import os
class Use:

    def __init__(self, convert: bool = False):
        # Utility will be added to convert to number format to be used for the ML
        self.convert = convert


    def check_time_formatting(time: str = "") -> bool:
        if time.count("_") != 2 or len(time) != 22 or time[8] != "_" or time[15] != "_":
            return False
        
        allowed_chars = list(range(0,10))
        allowed_chars = [str(i) for i in allowed_chars]
        allowed_chars.append("_")

        for i in range(len(time)):
            if time[i] not in allowed_chars: return False

        return True
        
        
    def time_difference(self,time1, time2) -> float:
        """
        time_difference("20231208_000511_546018", "20231208_000411_546018")
        00:05:11, 00:04:11

        Converted to seconds, ex: 60
        (also works for microseconds outputting a float)
        """

        datetime1 = datetime.strptime(time1, "%Y%m%d_%H%M%S_%f")
        datetime2 = datetime.strptime(time2, "%Y%m%d_%H%M%S_%f")

        if datetime1 > datetime2:
            datetime1, datetime2 = datetime2, datetime1
        #print(datetime1, datetime2)
        delta = datetime2 - datetime1

        return delta.total_seconds()

    def read_file(self, input_file: str="", delimiter: str="|") -> list:
        """
        input_file name:
        /home/computer/Documents/Output/TrackKeyboard_20231208_021718_368217.txt
        
        File contents:
        20231208_004930_177528|on_keypress|Key pressed: s
        20231208_004930_227942|on_keypress|Key pressed: d
        20231208_004930_279579|on_keypress|Key pressed: f
        20231208_004931_434505|on_keypress|Key pressed: c
        
        Output of function:
        [[0.550266, 'on_keypress', 'Key pressed: s'],
        ....
         [0.893151, 'on_keypress', 'Key pressed: c']]

        """

        if "" in [input_file, delimiter]: return []

        _, filename = os.path.split(input_file)
        start_time = filename.split(".")[0][-22:]

        with open(input_file, "r") as file: lines = file.read().split("\n")[:-1]

        list_return = []
        for line in lines:
            if line == [] or line.count(delimiter) == 0: continue

            append_line = line.split(delimiter)
            end_time = append_line[0]
            append_line[0] = self.time_difference(append_line[0], start_time)
            start_time = end_time
            
            list_return.append(append_line)
        return list_return





    #Make a converter for ML + converter to second time
        

#print(Use().read_file("/home/blender/Documents/updated_/Output/TrackKeyboard_20231208_004929_627262.txt"))

#test = ["20231208_000411_546018","202_31208_000411_546018","2023208_0004111_546018"]
#for i in test: print(Use.check_time_formatting(i))

"""
import time
test = [["20231208_000511_546018", "20231208_000521_546018"],
        ["20231208_000411_546014", "20231208_000411_546018"],
        ["20131208_000411_546018", "20231208_000411_546018"]]
for i in test:
    float1 = Use.time_difference(i[0], i[1])
    print(float1)
    time.sleep(float1)
"""
