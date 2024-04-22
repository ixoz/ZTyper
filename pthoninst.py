import subprocess
import os

# Get the directory of the current script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the relative path to the installer
installer_path = os.path.join(current_directory, "Python_Install", "python-3.12.3-amd64.exe")

# Check if the installer exists
if os.path.exists(installer_path):
    subprocess.Popen(installer_path)
else:
    print("Installer not found:", installer_path)
