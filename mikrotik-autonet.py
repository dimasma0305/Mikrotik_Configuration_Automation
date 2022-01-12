import paramiko
import time
from Modules.SD_Bridge import SD_Bridge

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
addr=input(str("Input Mikrotik ip address : "))
usr=input(str("Input username : "))
pswd=input(str("Input password : "))
ssh.connect(hostname=addr, username=usr, password=pswd)
stdin, stdout, stderr = ssh.exec_command(SD_Bridge)
print(stdout.read().decode("ascii").strip("\n"))

ssh.close()