import shlex, subprocess

command_line = './api'
args = shlex.split(command_line)
print(args)
p = subprocess.Popen(args)
print("oooooooooooooooooooooooooooooooooooooooooooooooo")