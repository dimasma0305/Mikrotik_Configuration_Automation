 /ip dhcp-client print
 /ip dhcp-client add interface=ether1 disable=no
 
 /interface bridge
 add name=bridge1
 /interface bridge port
 add bridge=bridge1 interface=ether2
 add bridge=bridge1 interface=ether3
 add bridge=bridge1 interface=ether4
 add bridge=bridge1 interface=ether5
 add bridge=bridge1 interface=ether6
 add bridge=bridge1 interface=ether7
 add bridge=bridge1 interface=ether8

 /ip address add interface=bridge1 address=192.168.100.1/24
 /ip route add gateway=bridge1
 
 /ip dns set servers=1.1.1.1
 /ip dns set allow-remote-request=yes
  
 /ip firewall nat add chain=srcnat out-interface=ether1 action=masquerade
 /ip firewall nat print
 
Setup DHCP Server dapat menggunakan

 /ip dhcp-server setup

Chat saat konfigurasi DHCP Server

 Select interface to run DHCP server on 
 dhcp server interface: '''bridge1''' - ketik nama bridge interface

 Select network for DHCP addresses 
 dhcp address space: '''192.168.100.0/24''' - sesuai IP bridge1 & [ENTER]

 Select gateway for given network 
 gateway for dhcp network: '''192.168.100.1''' - sesuai IP bridge1 & [ENTER]

 Select pool of ip addresses given out by DHCP server 
 addresses to give out: '''192.168.100.2-192.168.100.254''' - [ENTER]

 Select DNS servers 
 dns servers: '''192.168.1.1''' - [ENTER] - bisa 8.8.8.8

 Select lease time 
 lease time: 10m - [ENTER]

Aktifkan DHCP Server

 /ip dhcp-server enable
 /ip dhcp-server print


==Cek Client Connection==

Di VPCS1, cek sambungan dapat menggunakan perintah

 show ip   - lihat apakah VPCS dapat / mempunyai IP address
 ip dhcp   - untuk meminta IP address ke DHCP Server.
 ping x.x.x.x - ping ke IP x.x.x.x

atau set menggunakan IP statik

 ip 192.168.100.x/24 192.168.100.1 

Dimana

 192.168.100.x/24 - IP address client di konfigurasi Mikrotik di atas adalah keluarga 192.168.100.x/24
 192.168.100.1    - IP address gateway di jaringan

Di kali linux, cek sambungan dapat menggunakan perintah

 netstat -nr   - lihat tabel routing
 ifconfig      - lihat konfigurasi jaringan
 dhclient eth0 - meminta IP address ke DHCP Server

Biasanya kali linux akan lebih reliable daripada VPCS.

# Sumber
https://lms.onnocenter.or.id/wiki/index.php?title=Mikrotik:_Router_Sederhana&action=edit
