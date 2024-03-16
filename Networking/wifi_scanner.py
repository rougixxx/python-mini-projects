from wifi import Cell


# my wifi interface name: wlp4s0 
wifi_nets = Cell.all("wlp4s0")


for net in wifi_nets:
    print(f"\t Network Name: {net.ssid}")
    print(f"\t MAC: {net.address}\t Quality: {net.signal}")
    print(f"\t CHANNEL: {net.channel}\tFrequency: {net.frequency} ")
    if net.encrypted:
        print("\t The Wifi network has a Password")
        print(f"\t Security Type: {net.encryption_type}")
    else: 
        print("\t The Wifi Network has no Password")
    
    print(f"\t The Network Signal Value: {net.signal}")
    print(f"\t The Network Mode: {net.mode}")
    print("---------------------------------------------------------------------------")



