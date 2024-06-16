from bitarray import bitarray

class BinaryBytes:

    def __init__(self, bytes_data: bytes):
        self.bytes_data = bytes_data

    def __str__(self):
        return ''.join(format(byte, '08b') for byte in self.bytes_data)
    
    def to_bits_array(self) -> list[bool]:
        bits = [self.access_bit(self.bytes_data,i) == 1 for i in range(len(self.bytes_data)*8)]
        return bits
    
    def access_bit(self, data, num):
        base = int(num // 8)
        shift = int(num % 8)
        return (data[base] >> shift) & 0x1
    
class BinaryString:

    def __init__(self, string_data: str):
        self.string_data = string_data

    def __str__(self):
        return self.string_data
    
    def str_to_bytes(self) -> bytes:
        return self.bool_to_bytes([1 if c == '1' else 0 for c in self.string_data])
    
    def bool_to_bytes(self, bits: list[bool]) -> bytes:
        ba = bitarray(bits)
        return ba.tobytes()
    
    def bytes_to_string(self, bytes_data: bytes, encoding: str = "utf-8") -> str:
        return bytes_data.decode(encoding)
    
    def bytes_to_encoding(self, encoding: str = "utf-8"):
        print(f"Encoding: {encoding}")
        print(f"String: {self.string_data}")
        
        bytez  = self.str_to_bytes()
        print(f"Bytes: {bytez}")

        string = self.bytes_to_string(bytez, encoding)
        print(f"Decoded: {string}")
        return string   