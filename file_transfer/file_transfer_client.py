# Experiment 9: File Transfer Client
import socket

def client_program():
    host = socket.gethostname()
    port = 5000
    filename = 'file_to_send.txt' # Create this file

    with open(filename, 'w') as f:
        f.write("This is a test file for transfer.")

    client_socket = socket.socket()
    client_socket.connect((host, port))

    with open(filename, 'rb') as f:
        data = f.read(1024)
        while data:
            client_socket.send(data)
            data = f.read(1024)

    client_socket.close()
    print("File sent successfully.")

if __name__ == '__main__':
    client_program()
