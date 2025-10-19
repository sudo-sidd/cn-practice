# Experiment 6: UDP Client
import socket

def client_program():
    host = socket.gethostname()
    port = 5000
    server = (host, port)
    
    client_socket = socket.socket(type=socket.SOCK_DGRAM)
    
    message = input(" -> ")
    client_socket.sendto(str.encode(message), server)
    
    data, addr = client_socket.recvfrom(1024)
    data = data.decode()
    print('Received from server: ' + data)
    
    client_socket.close()

if __name__ == '__main__':
    client_program()
