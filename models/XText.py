from typing import List

class XText:

    def __init__(self, text: str, encoding: str = "utf-8"):
        self.text = text
        self.encoding = encoding

    def __str__(self) -> str:
        return self.text
    
    def to_bytes(self) -> bytes:
        return self.text.encode(self.encoding)

    def to_bits_str(self) -> str:
        return bin(int.from_bytes(self.to_bytes(), byteorder="big")).lstrip('0b')

    def to_bits_array(self) -> List[bool]:
        return [i == "1" for i in self.to_bits_str()]