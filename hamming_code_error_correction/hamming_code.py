# Experiment 20: Hamming Code
def hamming_code(data):
    d = list(map(int, data))
    n = len(d)
    
    # Calculate number of parity bits
    r = 1
    while 2**r < n + r + 1:
        r += 1
        
    # Create array for hamming code
    h = [0] * (n + r)
    j = 0
    k = 0
    for i in range(1, n + r + 1):
        if i == 2**j:
            j += 1
        else:
            h[i-1] = d[k]
            k += 1
            
    # Calculate parity bits
    for i in range(r):
        p = 2**i
        val = 0
        for j in range(1, n + r + 1):
            if j & p:
                val ^= h[j-1]
        h[p-1] = val
        
    return "".join(map(str, h))

def hamming_check(data):
    d = list(map(int, data))
    n = len(d)
    r = 0
    while 2**r < n + 1:
        r += 1
        
    error_pos = 0
    for i in range(r):
        p = 2**i
        val = 0
        for j in range(1, n + 1):
            if j & p:
                val ^= d[j-1]
        if val != 0:
            error_pos += p
            
    return error_pos

if __name__ == '__main__':
    data = "1011"
    encoded = hamming_code(data)
    print(f"Original data: {data}")
    print(f"Hamming code: {encoded}")
    
    # Introduce an error
    error_encoded = list(encoded)
    error_encoded[4] = '1' if error_encoded[4] == '0' else '0'
    error_encoded = "".join(error_encoded)
    print(f"Encoded with error: {error_encoded}")
    
    error_position = hamming_check(error_encoded)
    if error_position == 0:
        print("No error detected.")
    else:
        print(f"Error detected at position: {error_position}")
