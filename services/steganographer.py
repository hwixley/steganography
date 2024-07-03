from models.XEncoder import XEncoder
from models.XImage import XImage
from models.XText import XText
import numpy as np
from typing import Optional, Tuple
from base64 import b64encode, b64decode

class Steganographer:

    encoder: XEncoder
    
    def __init__(self, encoder: XEncoder = XEncoder()):
        self.encoder = encoder

    def encode_text_to_image(self, text: str, image_path: str) -> Tuple[np.ndarray, str]:
        image = XImage(fname=image_path)
        bitmask = XText(text).to_bits_array()
        
        encoded, offset = self.encoder.encode(data=image.pixels, bitmask=bitmask)
        key = self.obf_key(text=f"{len(bitmask)}-{offset}")
        
        return encoded, key

    def decode_text_from_image(self, image_path: str, key: str) -> str:
        image = XImage(fname=image_path)
        length, offset = self.deobf_key(obf_text=key)

        decoded_bitstr = self.encoder.decode(encoded=image.pixels, length=length, offset=offset)
        
        return self.encoder.bits_to_encoding(bitstr=decoded_bitstr)

    def obf_key(self, text: str) -> str:
        return b64encode(text.encode()).decode()
    
    def deobf_key(self, obf_text: str) -> Tuple[int, int]:
        deobf = b64decode(obf_text.encode()).decode()
        vals = deobf.split("-")
        return int(vals[0]), int(vals[1])