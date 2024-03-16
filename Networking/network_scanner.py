from scapy.all import ARP, Ether, srp
# theseare methods from the module  'scapy.all' of the scapy  library


# scan and netwok and give u details about ur network

def scan(ip):
    arp_req = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff") # broadcast Layer 2
    arp_broadcast = broadcast/arp_req
    result = srp(arp_broadcast, timeout=3, verbose=True)[0] # the index 0 is for getting only the machines that replaye to arp request
    # False for Not returning details
    print(result)
    lst = []
    for item in result:
        clients = {"ip": item[1].psrc, 'mac': item[1].hwsrc }
        lst.append(clients)
       

    print("IP \t\t\t\t\t MAC")
    print("-------------------------------------------------------------")
    for i in lst:
        print(f"{i['ip']} \t\t\t\t {i['mac']}")

ip = "192.168.14.1/24"
scan(ip)

