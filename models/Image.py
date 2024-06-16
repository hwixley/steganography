from PIL import Image
#import Image 
import numpy as np
from math import prod
from enum import Enum
from typing import Optional, List

class XImage:

    class Bitmap(str, Enum):
        PARITY = "parity"

        def get(self, a):
            if self == self.PARITY:
                return a % 2 == 0

    def __init__(self, fname: str, bitmap: Bitmap = Bitmap.PARITY):
        self.fname = fname
        self.bitmap = bitmap
        self.pixels = self.load_image()

    def load_image(self) -> np.ndarray:
        img = Image.open(self.fname)
        return np.array(img)

    def num_pixels(self) -> int:
        return prod(self.pixels.shape)
    
    def get_bitmap(self, bitmap: Optional[Bitmap] = None) -> np.ndarray:
        bool_map = (bitmap or self.bitmap).get(self.pixels)
        return bool_map

    def bitmap_encode(self, bits: list[bool]) -> np.ndarray:
        img = self.pixels
        shape = img.shape
        
        if len(bits) > prod(shape):
            print(f"ERROR: bitmap ({len(bits)}) is larger than image ({prod(shape)})")
            return

        idx = 0
        for i in range(shape[0]):
            for j in range(shape[1]):
                for k in range(shape[2]):
                    val = img[i,j,k]
                    if self.bitmap.get(val) != (bits[idx] == 1):
                        img[i,j,k] += -1 if val > 0 else 1
                    idx += 1

                    if idx >= len(bits):
                        return img

    def save(self, arr, fname):
        img = Image.fromarray(arr)
        img.save(fname)

    def bitmap_decode(self, encoded: np.ndarray) -> str:
        bitmap = self.bitmap.get(encoded)
        mask = bitmap.flatten()
        s = "".join(["1" if b else "0" for b in mask])
        return s

