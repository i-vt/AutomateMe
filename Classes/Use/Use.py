from datetime import datetime

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
        
        
        
    
    def time_difference(time1, time2) -> float:
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

        delta = datetime2 - datetime1

        return delta.total_seconds()
        

        
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
