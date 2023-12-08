import datetime, os, inspect
class Track:
    def __init__(self, output_option: str = "default", 
                output_folder: str = "", 
                delim: str = "|",
                extension: str = "txt"):
        """
        Valid output_option choices:
        - default: outpout to ./Output/TrackMouse_YYYYMMDD_hhmmss.txt; argument: none
        - custom: pick a new path, but pick using args
        - SQL: configs for an integration
        """
        valid_output_options = ["default", "custom"]
        if output_option not in valid_output_options:  raise ValueError
        if output_folder == "": 
            script_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
            output_folder = os.path.join(script_dir, "Output/")
        
        self.output_option = output_option
        self.output_folder = output_folder

        output_file = f"{self.__class__.__name__}_{self.now()}.{extension}"

        if not os.path.exists(output_folder): os.makedirs(output_folder)

        self.output_path = os.path.join(output_folder, output_file)

        self.delim = delim

    def now(self) -> str:
        current_time = datetime.datetime.now()
        formatted_string = current_time.strftime("%Y%m%d_%H%M%S_%f")
        return formatted_string


    def write(self, text):
        """
        assuming default self.delim  "|"
        function|args1|agrs2|...|argsn
        """

        with open(self.output_path, "a") as file: 
            file.write(self.now() + self.delim + str(text)+"\n")


 
# Test
# TrackMouse().record()

#Track().write(123)