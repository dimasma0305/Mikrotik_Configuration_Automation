import paramiko
import time

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
addr=input(str("Input Mikrotik ip address : "))
usr=input(str("Input username : "))
pswd=input(str("Input password : "))
ssh.connect(hostname=addr, username=usr, password=pswd)
stdin, stdout, stderr = ssh.exec_command("""
        ip address print
        ip dns set allow-remote-request=yes servers=8.8.8.8; ip dns print
        ip firewall nat add chain=srcnat action=masquerade; ip firewall nat print
        """)
print(stdout.read().decode("ascii").strip("\n"))

ssh.close()
