# Experiment 12: RARP Simulation
# This is a conceptual simulation.

rarp_table = {
    "00:1A:2B:01:02:03": "192.168.1.10",
    "00:1A:2B:04:05:06": "192.168.1.11"
}

def get_ip_address(mac_address):
    if mac_address in rarp_table:
        return rarp_table[mac_address]
    else:
        return "IP not found"

if __name__ == '__main__':
    mac1 = "00:1A:2B:01:02:03"
    mac2 = "00:1A:2B:04:05:06"
    mac3 = "00:1A:2B:07:08:09"

    print(f"IP for {mac1}: {get_ip_address(mac1)}")
    print(f"IP for {mac2}: {get_ip_address(mac2)}")
    print(f"IP for {mac3}: {get_ip_address(mac3)}")
