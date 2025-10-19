# Experiment 18: Selective Repeat
# This is a conceptual implementation.
import random
import time

def selective_repeat(total_frames, window_size):
    sent = [False] * total_frames
    acked = [False] * total_frames
    base = 0
    
    while base < total_frames:
        # Send frames in window
        for i in range(base, min(base + window_size, total_frames)):
            if not sent[i]:
                print(f"Sending frame {i}")
                sent[i] = True
        
        # Simulate acknowledgments (can be out of order)
        for i in range(base, min(base + window_size, total_frames)):
            if sent[i] and not acked[i]:
                if random.random() > 0.3: # 70% chance of ACK
                    print(f"Received ACK for frame {i}")
                    acked[i] = True
        
        # Slide window
        while base < total_frames and acked[base]:
            base += 1
            
        # Resend unacked frames
        for i in range(base, min(base + window_size, total_frames)):
            if not acked[i]:
                print(f"Resending frame {i}")
                sent[i] = True

        time.sleep(1)

if __name__ == '__main__':
    selective_repeat(total_frames=10, window_size=4)
