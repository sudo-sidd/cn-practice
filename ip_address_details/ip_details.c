# Experiment 4: C Program for IP address details
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netdb.h>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <hostname>\n", argv[0]);
        return 1;
    }

    char *hostname = argv[1];
    struct hostent *host;
    char ip_address[16];

    host = gethostbyname(hostname);
    if (host == NULL) {
        herror("gethostbyname");
        return 1;
    }

    inet_ntop(AF_INET, host->h_addr_list[0], ip_address, sizeof(ip_address));

    printf("Hostname: %s\n", host->h_name);
    printf("IP Address: %s\n", ip_address);

    return 0;
}
