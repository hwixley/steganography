from bitarray import bitarray
from typing import List

class BinaryBytes:

    def __init__(self, bytes_data: bytes):
        self.bytes_data = bytes_data

    def __str__(self):
        return bin(int.from_bytes(self.bytes_data, byteorder="big")).lstrip('0b')
    
    def to_bits_array(self) -> List[bool]:
        str_bin = self.__str__()
        bits = [i == "1" for i in str_bin]
        return bits
    
    # def access_bit(self, data, num):
    #     base = int(num // 8)
    #     shift = int(num % 8)
    #     return (data[base] >> shift) & 0x1

def bitstring_to_bytes(s):
    return int(s, 2).to_bytes((len(s) + 7) // 8, byteorder='big')
    
class BinaryString:

    def __init__(self, string_data: str):
        self.string_data = string_data

    def __str__(self):
        return self.string_data
    
    def str_to_bytes(self) -> bytes:
        return self.bool_to_bytes([c == '1' for c in self.string_data])
    
    def bool_to_bytes(self, bits: List[bool]) -> bytes:
        ba = bitarray(bits)
        return ba.tobytes()
    
    def bytes_to_string(self, bytes_data: bytes, encoding: str = "utf-8") -> str:
        return bytes_data.decode(encoding)
    
    def bytes_to_encoding(self, encoding: str = "utf-8"):
        print(f"Encoding: {encoding}")
        # print(f"String: {self.string_data}")
        print(len(self.string_data))
        with open("bin.txt", "w") as f:
            f.write(self.string_data)
        
        bytez  = bitstring_to_bytes(s=self.string_data) # self.str_to_bytes()
        # print(f"Bytes: {bytez}")

        string = self.bytes_to_string(bytez, encoding)
        print(f"Decoded: {string}")
        return string   