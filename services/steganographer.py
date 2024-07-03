from models.XEncoder import XEncoder
from models.XImage import XImage
from models.XText import XText
from services.cryptographer import Cryptographer
import numpy as np
from typing import Tuple

class Steganographer:

    encoder: XEncoder
    
    def __init__(self, encoder: XEncoder = XEncoder()):
        self.encoder = encoder

    def encode_text_to_image(self, text: str, image_path: str) -> Tuple[np.ndarray, str]:
        image = XImage(fname=image_path)
        bitmask = XText(text).to_bits_array()
        
        encoded, offset = self.encoder.encode(data=image.pixels, bitmask=bitmask)
        key = Cryptographer.obf_key(text=f"{len(bitmask)}-{offset}")
        
        return encoded, key

    def decode_text_from_image(self, image_path: str, key: str) -> str:
        image = XImage(fname=image_path)
        length, offset = Cryptographer.deobf_key(obf_text=key)

        decoded_bitstr = self.encoder.decode(encoded=image.pixels, length=length, offset=offset)
        
        return self.encoder.bits_to_encoding(bitstr=decoded_bitstr)

