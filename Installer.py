import subprocess

# Define the path to your requirements.txt file
requirements_file = "requirements.txt"

# Use subprocess to run pip to install the packages
try:
    subprocess.check_call(["pip", "install", "-r", requirements_file])
    print("Packages installed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error: Failed to install packages. {e}")
