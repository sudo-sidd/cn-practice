# Experiment 17: Go-Back-N
# This is a conceptual implementation.
import random
import time

def go_back_n(total_frames, window_size):
    sent_frames = 0
    while sent_frames < total_frames:
        for i in range(sent_frames, min(sent_frames + window_size, total_frames)):
            print(f"Sending frame {i}")
        
        # Simulate acknowledgment
        ack_received = random.randint(sent_frames, sent_frames + window_size)
        
        if ack_received == sent_frames:
            print(f"Timeout for frame {sent_frames}. Resending window.")
            time.sleep(1)
            continue
        
        print(f"Received ACK for frame {ack_received - 1}")
        sent_frames = ack_received

if __name__ == '__main__':
    go_back_n(total_frames=10, window_size=4)
