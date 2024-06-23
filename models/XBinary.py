from bitarray import bitarray
from typing import List

def bitstring_to_bytes(s):
    return int(s, 2).to_bytes((len(s) + 7) // 8, byteorder='big')
    
class XBinaryString:

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
        bytez  = bitstring_to_bytes(s=self.string_data)
        string = self.bytes_to_string(bytez, encoding)
        
        print(f"Encoding: {encoding}")
        print(f"Decoded: {string}")
        return string   