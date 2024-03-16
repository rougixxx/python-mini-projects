import socket
from geoip import geolite2
from scapy.all import * 
import time

# wifi interface name: wlp4s0

# eth inteface name enp0s31f6



def get_serv(src_port, src_dst):
    try:
        service = socket.getservbyport(src_port)
    except:
        service = socket.getservbyport(src_dst)
    return service



def locate(ip):
    loc = geolite2.lookup(ip)
    if loc is not None :
        return loc.country, loc.timezone
    else:
        return None



def analyzer(pkt):

    try:
        src_ip = pkt[IP].src
        dst_ip = pkt[IP].dst 
       
        loc_src = locate(src_ip)
        loc_dst = locate(dst_ip)
        if loc_src is not None :
            country = loc_src[0]
            timezone = loc_src[1]
        elif loc_dst is not None: 
            country =  loc_dst[0]
            timezone = loc_dst[1]   
        else:
            country = "UNKNOWN"
            timezone = "UNKNOWN"
         
         
        mac_src = pkt.src
        mac_dst = pkt.dst

        if pkt.haslayer(ICMP):
            print("ICMP PACKET")
            print(f"Source IP: {src_ip} Destination IP: {dst_ip}")
            print(f"Timezone: {timezone}  Country: {country}")
            print(f"MAC Source: {mac_src}, MAC Destination: {mac_dst}")
            print(f"the Packet size is: {len(pkt[ICMP])} Bytes \n")
            if pkt.haslayer(Raw):
                print(f" the packet load: {pkt[Raw].load} ")
            print("----------------------------------------------")

        else: 
            src_port = pkt.sport 
            dst_port = pkt.dport 
            service = get_serv(src_port, dst_port)

            if pkt.haslayer(TCP):
                print("TCP PACKET")
                print(f"Source IP: {src_ip} Destination IP: {dst_ip}")
                print(f"Timezone: {timezone}  Country: {country}")
                print(f"The service is:  {service}")
                print(f"MAC Source: {mac_src}, MAC Destination: {mac_dst}")
                print(f"Source Port: {src_port}, Destination Port: {dst_port}")
                print(f"the Packet size is: {len(pkt[TCP])} Bytes \n")
                if pkt.haslayer(Raw):
                    print(f" the packet load: {pkt[Raw].load}")
                print("----------------------------------------------")
            if pkt.haslayer(UDP):
                print("UDP PACKET")
                print(f"Source IP: {src_ip} Destination IP: {dst_ip}")
                print(f"MAC Source: {mac_src}, MAC Destination: {mac_dst}")
                print(f"Source Port: {src_port}, Destination Port: {dst_port}")
                print(f"the Packet size is: {len(pkt[UDP])} Bytes \n")
                if pkt.haslayer(Raw):
                    print(f" the packet load: {pkt[Raw].load}")
                print("----------------------------------------------")
    except Exception as e  :
        print(e)

                
    
   

        

    time.sleep(1)

print("*************** STARTED the Operation*****************")
sniff(iface="enp0s31f6", prn=analyzer)
# sniff(iface="wlp4s0", prn=analyzer)


