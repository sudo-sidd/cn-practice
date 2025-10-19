# Experiment 8: Full Duplex Chat Server
import socket
import threading

def receive_messages(conn):
    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                break
            print("Client: " + data)
        except:
            break

def server_program():
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))

    thread = threading.Thread(target=receive_messages, args=(conn,))
    thread.start()

    while True:
        message = input()
        if message.lower() == 'bye':
            break
        conn.send(message.encode())

    conn.close()

if __name__ == '__main__':
    server_program()
