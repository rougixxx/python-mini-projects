from scapy.all import ARP, Ether, srp
import sys 
# improved version of the previus script

def scan(ip):
    exist = []
    while True:
        try:
            arp_req = ARP(pdst=ip)
            broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
            arp_broadcast = broadcast/arp_req
            result = srp(arp_broadcast, timeout=3, verbose=False)[0]
            clients_list = []
            
            for item in result:
                Client = {"ip": item[1].psrc, "mac": item[1].hwsrc}
                clients_list.append(Client)
            for item in clients_list:
                if item['mac'] not in exist:
                    print(f"{item['ip']} \t\t\t\t {item['mac']}\n")
                    exist.append(item['mac'])
        except KeyboardInterrupt:
            print("Exiting...!")
            sys.exit()
ip = str(input("Enter IP & Prefix with this Format IP/Prefix >>>: "))
print("\n")

scan(ip)
