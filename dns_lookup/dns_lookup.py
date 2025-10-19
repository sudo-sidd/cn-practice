# Experiment 10: DNS Lookup
import socket

def dns_lookup(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        print(f"The IP address of {hostname} is {ip_address}")
    except socket.gaierror:
        print(f"Could not resolve hostname: {hostname}")

if __name__ == '__main__':
    dns_lookup("www.google.com")
