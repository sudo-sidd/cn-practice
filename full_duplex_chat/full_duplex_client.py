# Experiment 8: Full Duplex Chat Client
import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            print("Server: " + data)
        except:
            break

def client_program():
    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    thread = threading.Thread(target=receive_messages, args=(client_socket,))
    thread.start()

    while True:
        message = input()
        if message.lower() == 'bye':
            break
        client_socket.send(message.encode())

    client_socket.close()

if __name__ == '__main__':
    client_program()
