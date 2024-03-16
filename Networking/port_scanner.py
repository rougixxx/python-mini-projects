import socket


target = "172.217.21.14"
ports = [19, 20, 21, 22,23, 24, 25, 80, 443]
open_ports = []
for p in range(1,101):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target,p))
    if result == 0:
        service = socket.getservbyport(p)
        open_ports.append({"Service": service, "Port": p })
        print(f"--[ * {p} * is open --> {service} ]")
    s.close()

for service in open_ports:
    print(service)
