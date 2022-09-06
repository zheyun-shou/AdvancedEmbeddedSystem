import shlex, subprocess
import time

command_line = 'sudo ./rock'
args = shlex.split(command_line)
print(args)
p = subprocess.Popen(args)
print("oooooooooooooooooooooooooooooooooooooooooooooooo")
time.sleep(10)
command_line = 'sudo ./paper'
args = shlex.split(command_line)
print(args)
q = subprocess.Popen(args)
print("++")
#Popen.kill()
