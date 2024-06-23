from models.XEncoder import XEncoder
from models.XImage import XImage
from models.XText import XText
import numpy as np
from typing import Optional, Tuple

class Steganographer:

    encoder: XEncoder
    
    def __init__(self, encoder: XEncoder = XEncoder()):
        self.encoder = encoder

    def encode_text_to_image(self, text: str, image_path: str) -> Tuple[np.ndarray,int]:
        image = XImage(fname=image_path)
        bitmask = XText(text).to_bits_array()
        return self.encoder.encode(data=image.pixels, bitmask=bitmask), len(bitmask)

    def decode_text_from_image(self, image_path: str, length: Optional[int] = None) -> str:
        image = XImage(fname=image_path)
        decoded_bitstr = self.encoder.decode(encoded=image.pixels, length=length)
        return self.encoder.bits_to_encoding(bitstr=decoded_bitstr)