# Experiment 6: UDP Server
import socket

def server_program():
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket(type=socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print("UDP server up and listening")

    while(True):
        bytesAddressPair = server_socket.recvfrom(1024)
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]
        clientMsg = "Message from Client:{}".format(message)
        clientIP  = "Client IP Address:{}".format(address)
        
        print(clientMsg)
        print(clientIP)
        
        server_socket.sendto(str.encode("Hello from UDP server"), address)

if __name__ == '__main__':
    server_program()
