HTB_bridge ='''
/interface bridge add name=virtual-switch
/interface bridge port add bridge=virtual-switch interface=ether2
/interface bridge port add bridge=virtual-switch interface=ether3
/interface bridge port add bridge=virtual-switch interface=ether4
/interface bridge port add bridge=virtual-switch interface=ether5
/interface bridge port add bridge=virtual-switch interface=ether6
/interface bridge port add bridge=virtual-switch interface=ether7
/interface bridge port add bridge=virtual-switch interface=ether8
/ip address add interface=virtual-switch address=192.168.56.20/24
/ip route add gateway=virtual-switch
/ip dns set servers=1.1.1.1
/ip dns set allow-remote-request=yes
/ip firewall nat add chain=srcnat out-interface=ether1 action=masquerade
/ip firewall mangle add comment="PC 1 CONNECTION" chain=prerouting action=mark-connection new-connection-mark=pc1-connection passthrough=yes src-address=192.168.56.1 in-interface=virtual-switch log=no log-prefix=""
/ip firewall mangle add comment="PC 2 CONNECTION" chain=prerouting action=mark-connection new-connection-mark=pc2-connection passthrough=yes src-address=192.168.56.2 in-interface=virtual-switch log=no log-prefix=""
/ip firewall mangle add comment="PC 3 CONNECTION" chain=prerouting action=mark-connection new-connection-mark=pc3-connection passthrough=yes src-address=192.168.56.3 in-interface=virtual-switch log=no log-prefix=""
/ip firewall mangle add comment="PC 1 UPLOAD" chain=prerouting action=mark-packet new-packet-mark=pc1-upload passthrough=yes connection-mark=pc1-connection in-interface=virtual-switch log=no log-prefix=""
/ip firewall mangle add comment="PC 2 UPLOAD" chain=prerouting action=mark-packet new-packet-mark=pc2-upload passthrough=yes connection-mark=pc2-connection in-interface=virtual-switch log=no log-prefix=""
/ip firewall mangle add comment="PC 3 UPLOAD" chain=prerouting action=mark-packet new-packet-mark=pc3-upload passthrough=yes connection-mark=pc3-connection in-interface=virtual-switch log=no log-prefix=""
/ip firewall mangle add comment="PC 1 DOWNLOAD" chain=postrouting action=mark-packet new-packet-mark=pc1-download passthrough=yes connection-mark=pc1-connection out-interface=virtual-switch log=no log-prefix="" 
/ip firewall mangle add comment="PC 2 DOWNLOAD" chain=postrouting action=mark-packet new-packet-mark=pc2-download passthrough=yes connection-mark=pc2-connection out-interface=virtual-switch log=no log-prefix=""
/ip firewall mangle add comment="PC 3 DOWNLOAD" chain=postrouting action=mark-packet new-packet-mark=pc3-download passthrough=yes connection-mark=pc3-connection out-interface=virtual-switch log=no log-prefix=""
/queue tree add name="parent-upload" parent=ether1 packet-mark="" limit-at=0 queue=default-small priority=8 max-limit=10M burst-limit=0 burst-time=0s bucket-size=0.1
/queue tree add name="parent-download" parent=ether2 packet-mark="" limit-at=0 queue=default-small priority=8 max-limit=10M burst-limit=0 burst-time=0s bucket-size=0.1
/queue tree add name="pc1-upload" parent=parent-upload packet-mark=pc1-upload limit-at=2M queue=default-small priority=7 max-limit=10M  burst-limit=0 burst-threshold=0 burst-time=0s bucket-size=0.1
/queue tree add name="pc1-download" parent=parent-download packet-mark=pc1-download limit-at=2M queue=default-small priority=7 max-limit=10M  burst-limit=0 burst-threshold=0 burst-time=0s bucket-size=0.1
/queue tree add name="pc2-upload" parent=parent-upload packet-mark=pc2-upload limit-at=2M queue=default-small priority=8 max-limit=10M burst-limit=0 burst-threshold=0 burst-time=0s bucket-size=0.1
/queue tree add name="pc2-download" parent=parent-download packet-mark=pc2-download limit-at=2M queue=default-small priority=8 max-limit=10M  burst-limit=0 burst-threshold=0 burst-time=0s bucket-size=0.1
/queue tree add name="pc3-upload" parent=parent-upload packet-mark=pc3-upload limit-at=2M queue=default-small priority=8 max-limit=10M burst-limit=0 burst-threshold=0 burst-time=0s bucket-size=0.1
/queue tree add name="pc3-download" parent=parent-download packet-mark=pc3-download limit-at=2M queue=default-small priority=8 max-limit=10M  burst-limit=0 burst-threshold=0 burst-time=0s bucket-size=0.1
'''