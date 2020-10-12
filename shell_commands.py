import subprocess

command = subprocess.call(['ls', '-l'])

# check_output nie wyswietla outputu
# wyswietli za to stderr dlatego jest przekierowany do stdout
# wyswietli tez stack trace pythona
cmd = subprocess.check_output(['ls', '-lhtr'], stderr=subprocess.STDOUT) 
print(cmd)
