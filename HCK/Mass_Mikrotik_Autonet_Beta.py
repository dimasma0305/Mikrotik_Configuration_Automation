import paramiko
import time

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
addr="192.168.122."#network id
hst=list(range(90,100))#host id pool
print(hst)
usr="admin"#username
pswd=""#password

for a in hst:
    try:
        ssh.connect(hostname=addr+str(a), username=usr, password=pswd, timeout=0.5)
        print(addr+str(a),"connected")
        stdin, stdout, stderr = ssh.exec_command("/ip ro pr")#perintah ssh
        print(stdout.read().decode("ascii").strip("\n"))
    except:
        print(addr+str(a), "timeout")
        continue
        

