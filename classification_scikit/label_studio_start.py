import subprocess
import os

# change the current directory
# to specified directory
os.chdir(r"../venv/Scripts")
p = subprocess.Popen("label-studio.exe --host http://192.127.0.0")
return_code = p.wait()
