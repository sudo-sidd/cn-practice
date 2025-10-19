# Experiment 16: Stop and Wait Sender
import socket
import time

def sender():
    host = '127.0.0.1'
    port = 65432
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        
        for i in range(5):
            message = f"Frame {i}"
            s.sendall(message.encode())
            print(f"Sent: {message}")
            
            s.settimeout(2) # Wait for ACK
            try:
                ack = s.recv(1024).decode()
                print(f"Received: {ack}")
            except socket.timeout:
                print("Timeout! Resending...")
                s.sendall(message.encode())
            
            time.sleep(1)

if __name__ == "__main__":
    sender()
