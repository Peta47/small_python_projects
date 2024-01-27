from scapy.all import ARP, Ether, srp
while True:
    ip_range = "192.168.1.0/24"

    def scan_local_network(ip_range):
        arp_request = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip_range)
        
        result = srp(arp_request, timeout=3, verbose=3)[0]

        used_ips = []
        for send, received in result:
            used_ips.append({'ip': received.psrc, 'mac': received.hwsrc})

        return used_ips

    used_ips = scan_local_network(ip_range)
    for entry in used_ips:
        print(f"IP adresa: {entry['ip']}, MAC adresa: {entry['mac']}")