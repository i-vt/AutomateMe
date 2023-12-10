import subprocess

if __name__ != "__main__": from .Use import Use as u
else: from Use import Use as u

class UseSystem(u):

    def execute_command(self, command: str="") -> dict:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        record = {
            "Command": command,
            "Output": output.decode('utf-8'),
            "Error": error.decode('utf-8')
        }
        return record

#UseSystem().execute_command("touch /home/computer/Downloads/1.txt")
