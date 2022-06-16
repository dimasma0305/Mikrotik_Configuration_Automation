import paramiko
import time
#parser = argparse.ArgumentParser()
#parser.add_argument('--foo', help='foo help')
#args = parser.parse_args()
#from Modules.SD_Bridge import SD_Bridge
from Modules.HTB_bridge import HTB_bridge

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
addr=input(str("Input Mikrotik ip address : "))
usr=input(str("Input username : "))
pswd=input(str("Input password : "))
ssh.connect(hostname=addr, username=usr, password=pswd)
stdin, stdout, stderr = ssh.exec_command(HTB_bridge)
print(stdout.read().decode("ascii").strip("\n"))

ssh.close()