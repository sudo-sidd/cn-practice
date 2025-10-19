# Experiment 15: Leaky Bucket Algorithm
import time

def leaky_bucket(packet_sizes, bucket_size, output_rate):
    storage = 0
    for size in packet_sizes:
        if size + storage > bucket_size:
            print(f"Packet of size {size} dropped (bucket overflow)")
        else:
            storage += size
            print(f"Packet of size {size} added to bucket. Storage: {storage}")
        
        leaked_amount = min(storage, output_rate)
        storage -= leaked_amount
        print(f"Leaked {leaked_amount}. Storage: {storage}")
        time.sleep(1)

if __name__ == '__main__':
    packets = [10, 20, 5, 15, 25]
    bucket_capacity = 30
    rate = 10
    leaky_bucket(packets, bucket_capacity, rate)
