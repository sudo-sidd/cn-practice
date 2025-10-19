# Experiment 19: CRC (Cyclic Redundancy Check)
def crc(data, divisor):
    data = list(data)
    divisor = list(divisor)
    
    for i in range(len(data) - len(divisor) + 1):
        if data[i] == '1':
            for j in range(len(divisor)):
                data[i+j] = str(int(data[i+j]) ^ int(divisor[j]))
                
    return "".join(data[-(len(divisor)-1):])

if __name__ == '__main__':
    dataword = "100100"
    generator = "1101"
    
    # Sender side
    appended_data = dataword + '0' * (len(generator) - 1)
    remainder = crc(appended_data, generator)
    codeword = dataword + remainder
    print(f"Remainder: {remainder}")
    print(f"Codeword: {codeword}")
    
    # Receiver side
    received_codeword = "100100101" # No error
    syndrome = crc(received_codeword, generator)
    print(f"Syndrome: {syndrome}")
    if int(syndrome) == 0:
        print("No error detected.")
    else:
        print("Error detected.")
