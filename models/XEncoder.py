import numpy as np
from math import prod
from bitarray import bitarray
from enum import Enum
from typing import Optional, List

class XEncoder:

    class Bitmap(str, Enum):
        PARITY = "parity"

        def get(self, a):
            if self == self.PARITY:
                return a % 2 == 0
            return None

    def __init__(self, bitmap: Bitmap = Bitmap.PARITY):
        self.bitmap = bitmap

    def encode(self, data: np.ndarray, bitmask: List[bool]) -> np.ndarray:
        shape = data.shape
        
        if len(bitmask) > prod(shape):
            print(f"ERROR: bitmap ({len(bitmask)}) is larger than data ({prod(shape)})")
            return

        idx = 0
        if len(shape) == 2:
            for i in range(shape[0]):
                for j in range(shape[1]):
                    val = data[i,j]
                    if self.bitmap.get(val) != bitmask[idx]:
                        data[i,j] += -1 if val > 0 else 1
                    idx += 1

                    if idx >= len(bitmask):
                        return data
        elif len(shape) == 3:
            for i in range(shape[0]):
                for j in range(shape[1]):
                    for k in range(shape[2]):
                        val = data[i,j,k]
                        if self.bitmap.get(val) != bitmask[idx]:
                            data[i,j,k] += -1 if val > 0 else 1
                        idx += 1

                        if idx >= len(bitmask):
                            return data

    def decode(self, encoded: np.ndarray, length: Optional[int] = None) -> str:
        bitmap = self.bitmap.get(encoded)
        mask = bitmap.flatten()
        s = "".join(["1" if b else "0" for b in mask])
        return s[:length]
    
    def bits_to_encoding(self, bitstr: str, encoding: str = "utf-8") -> str:
        bitstr_bytes = int(bitstr, 2).to_bytes((len(bitstr) + 7) // 8, byteorder='big')
        return bitstr_bytes.decode(encoding=encoding)