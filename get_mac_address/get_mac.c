# Experiment 3: C Program to retrieve MAC address
#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/ioctl.h>
#include <net/if.h>
#include <unistd.h>

int main() {
    struct ifreq ifr;
    int sock;
    char *iface = "eth0"; // Change this to your network interface

    sock = socket(AF_INET, SOCK_DGRAM, 0);
    if (sock == -1) {
        perror("socket");
        return 1;
    }

    ifr.ifr_addr.sa_family = AF_INET;
    strncpy(ifr.ifr_name, iface, IFNAMSIZ - 1);

    if (ioctl(sock, SIOCGIFHWADDR, &ifr) == -1) {
        perror("ioctl");
        close(sock);
        return 1;
    }

    close(sock);

    unsigned char *mac = (unsigned char *)ifr.ifr_hwaddr.sa_data;

    printf("MAC address for %s: %.2x:%.2x:%.2x:%.2x:%.2x:%.2x\n",
           iface, mac[0], mac[1], mac[2], mac[3], mac[4], mac[5]);

    return 0;
}
