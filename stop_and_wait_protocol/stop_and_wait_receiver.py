# Experiment 16: Stop and Wait Receiver
import socket

def receiver():
    host = '127.0.0.1'
    port = 65432
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Received: {data.decode()}")
                ack = f"ACK for {data.decode()}"
                conn.sendall(ack.encode())
                print(f"Sent: {ack}")

if __name__ == "__main__":
    receiver()
