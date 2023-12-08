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
        
        if output_folder == "": output_folder = "Output/"       
        self.output_option = output_option


        output_file = f"{self.__class__.__name__}_{self.now()}.{extension}"

        self.output_path = self.make_local_folder_get_filepath(output_folder, output_file)
        self.delim = delim

    def make_local_folder_get_filepath(self, folder: str="", filename: str="") -> str:
        if folder == "": folder = "UnknownFolder"
        script_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        output_folder = os.path.join(script_dir, folder)
        output_file = filename
        
        if not os.path.exists(output_folder): os.makedirs(output_folder)

        if output_file != "": return os.path.join(output_folder, output_file)
        else: return output_folder


    def now(self) -> str:
        """
        self.now() -> 20231208_000411_546018
        """
        current_time = datetime.datetime.now()
        formatted_string = current_time.strftime("%Y%m%d_%H%M%S_%f")
        return formatted_string


    def write(self, text):
        """
        Output produced, assuming default self.delim  "|":
        20231208_000411_546018|Text passed goes here
        """

        with open(self.output_path, "a") as file: 
            file.write(self.now() + self.delim + str(text)+"\n")

    """
    # Dynamic function naming, commented out b/c when inherited it prints:
    # <bound method Track.function_name of <__main__.TrackKeyboard object at 0x1232342>>
    def function_name(self) -> str:
        current_frame = inspect.currentframe()
        function_name = inspect.getframeinfo(current_frame).function
        output = str(function_name)
        return output
    """
    def write_record(self, *args):
        """
        write_record("Text passed goes here", 1 , "AAAA")
        Output produced, assuming default self.delim  "|":
        20231208_000411_546018|Text passed goes here|1|AAAA
        """

        output = ""
        for arg in args:
            output += f"{self.delim}{arg}"

        if len(output) > 1: output = output[1:]

        self.write(output) 

        
