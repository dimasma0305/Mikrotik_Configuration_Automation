import paramiko
import time

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="192.168.122.213", username="admin")
stdin, stdout, stderr = ssh.exec_command("ip address print")
print(stdout.read().decode("ascii").strip("\n"))

ssh.close()