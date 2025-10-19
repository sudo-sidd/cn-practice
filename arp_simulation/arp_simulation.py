# Experiment 11: ARP Simulation
# This is a conceptual simulation. Python's standard library
# does not provide a direct way to interact with ARP tables.
# This script simulates the logic.

arp_table = {}

def get_mac_address(ip_address):
    if ip_address in arp_table:
        return arp_table[ip_address]
    else:
        # In a real scenario, this would broadcast an ARP request.
        # Here, we'll just simulate adding it.
        print(f"Simulating ARP request for {ip_address}")
        mac_address = f"00:1A:2B:{ip_address.split('.')[-1]}:{ip_address.split('.')[-2]}:{ip_address.split('.')[-3]}"
        arp_table[ip_address] = mac_address
        return mac_address

if __name__ == '__main__':
    ip1 = "192.168.1.1"
    ip2 = "192.168.1.2"

    print(f"MAC for {ip1}: {get_mac_address(ip1)}")
    print(f"MAC for {ip2}: {get_mac_address(ip2)}")
    print(f"MAC for {ip1} (cached): {get_mac_address(ip1)}")
    print("ARP Table:", arp_table)
