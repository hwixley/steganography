import numpy as np
from bitarray import bitarray

class Encoder:

    def __init__(self, message: str):
        self.message = message

    def str_to_bytes(self, val: str):
        return bitarray(val).tobytes()

    def binary_str(self, encoding: str = "ascii"):
        # Encode the string to bytes using the specified encoding
        byte_data = self.message.encode(encoding)
        
        # Convert the bytes to a binary string
        binary_string = ''.join(format(byte, '08b') for byte in byte_data)
        print(bytes(binary_string))

        # Adjust the binary string to the specified length
        # if length is not None:
        #     if len(binary_string) > length:
        #         # Truncate the binary string if it is longer than the specified length
        #         binary_string = binary_string[:length]
        #     else:
        #         # Pad the binary string with zeros if it is shorter than the specified length
        #         binary_string = binary_string.ljust(length, '0')
        
        return binary_string

    def binary_bool(self):
        vals = np.array(list(self.binary_str()))
        return np.equal(vals, np.array(["0"]*len(vals)))

    def binary_to_str(self, arr, encoding: str = "utf-8"):
        binary_string = self.blist_to_bstr(arr=arr)

        if len(binary_string) % 8 != 0:
            raise ValueError("The length of the binary string should be a multiple of 8.")

        # Split the binary string into bytes (8 bits each)  
        byte_chunks = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
        
        # Convert each byte chunk from binary to integer
        byte_data = bytes(int(byte, 2) for byte in byte_chunks)
        print(byte_data[:20])
        
        try:
            # Decode the bytes to a string using the specified encoding
            text_string = byte_data.decode(encoding)
        except UnicodeDecodeError as e:
            raise ValueError(f"Failed to decode the binary string with encoding {encoding}: {e}")
        
        return text_string

    def blist_to_bstr(self, arr):
        # print(len(arr))
        # print("Hi")
        return "".join(["" if i+1 % 8 == 0 else "" + ("1" if a else "0") for i, a in enumerate(arr)])