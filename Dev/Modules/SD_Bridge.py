SD_Bridge=  """
            /ip dhcp-client print
            /interface bridge
            /interface bridge add name=bridge1
            /interface bridge port
            /interface bridge port add bridge=bridge1 interface=ether2
            /interface bridge port add bridge=bridge1 interface=ether3
            /interface bridge port add bridge=bridge1 interface=ether4
            /interface bridge port add bridge=bridge1 interface=ether5
            /interface bridge port add bridge=bridge1 interface=ether6
            /interface bridge port add bridge=bridge1 interface=ether7
            /interface bridge port add bridge=bridge1 interface=ether8
            /ip address add interface=bridge1 address=192.168.100.1/24
            /ip route add gateway=bridge1
            /ip dns set servers=8.8.8.8
            /ip dns set allow-remote-request=yes
            /ip firewall nat add chain=srcnat out-interface=ether1 action=masquerade
            /ip firewall nat print
            /ip dhcp-server setup
            /ip dhcp-server enable
            /ip dhcp-server print
            """