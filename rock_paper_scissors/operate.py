import shlex, subprocess

command_line = 'sudo ./rock'
args = shlex.split(command_line)
print(args)
p = subprocess.Popen(args)
print("oooooooooooooooooooooooooooooooooooooooooooooooo")
#Popen.kill()
