import numpy as np
from math import prod
from bitarray import bitarray
from enum import Enum
from typing import Optional, List, Tuple
from random import randint

class XEncoder:

    class Bitmap(str, Enum):
        PARITY = "parity"

        def get(self, a):
            if self == self.PARITY:
                return a % 2 == 0
            return None

    def __init__(self, bitmap: Bitmap = Bitmap.PARITY):
        self.bitmap = bitmap

    def encode(self, data: np.ndarray, bitmask: List[bool], offset: int = -1) -> Tuple[np.ndarray, int]:
        shape = data.shape
        
        if len(bitmask) > prod(shape):
            print(f"ERROR: bitmap ({len(bitmask)}) is larger than data ({prod(shape)}). Please try again.")
            return

        max_offset = prod(shape) - len(bitmask)
        if offset == -1:
            offset = randint(0, max_offset)
        elif offset < -1 or offset > max_offset:
            print(f"ERROR: bitmap offset ({offset}) is out of range of the data. The possible values are in the range [0,{max_offset}], or choosing -1 will randomly assign an offset. Please try again.")
            return

        iter_idx = 0
        bm_idx = 0
        if len(shape) == 2:
            for i in range(shape[0]):
                for j in range(shape[1]):
                    if iter_idx >= offset:
                        val = data[i,j]
                        if self.bitmap.get(val) != bitmask[bm_idx]:
                            data[i,j] += -1 if val > 0 else 1
                        bm_idx += 1

                        if bm_idx >= len(bitmask):
                            return data, offset

                    iter_idx += 1

        elif len(shape) == 3:
            for i in range(shape[0]):
                for j in range(shape[1]):
                    for k in range(shape[2]):
                        if iter_idx >= offset:
                            val = data[i,j,k]
                            if self.bitmap.get(val) != bitmask[bm_idx]:
                                data[i,j,k] += -1 if val > 0 else 1
                            bm_idx += 1

                            if bm_idx >= len(bitmask):
                                return data, offset
                        
                        iter_idx += 1

    def decode(self, encoded: np.ndarray, length: Optional[int] = None, offset: int = 0) -> str:
        end_idx = offset + length if length is not None else None
        encoded = encoded.flatten()[offset: end_idx]
        bitmap = self.bitmap.get(encoded)
        mask = bitmap.flatten()
        s = "".join(["1" if b else "0" for b in mask])
        return s
    
    def bits_to_encoding(self, bitstr: str, encoding: str = "utf-8") -> str:
        try:
            bitstr_bytes = int(bitstr, 2).to_bytes((len(bitstr) + 7) // 8, byteorder='big')
            return bitstr_bytes.decode(encoding=encoding)
        except Exception:
            print("ERROR: cannot decode the data to text, you have input something wrong, exiting...")
            exit(1)