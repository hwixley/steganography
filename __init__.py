from PIL import Image
import numpy as np
from models.XImage import XImage
from models.XText import XText
from models.XBinary import XBinaryString
from models.XEncoder import XEncoder

def save(arr: np.ndarray, fname: str):
    Image.fromarray(arr).save(fname)


encoder = XEncoder()
image = XImage(fname="sample.png")
text = XText(text="Hello good sir this is a dear message that I hope finds you well I hope the supplementary image was complementary tooProps on getting to this point it means the script must have worked")


if __name__ == "__main__":
    bitmask = text.to_bits_array()
    encoded = encoder.encode(data=image.pixels, bitmask=bitmask)

    save(arr=encoded, fname="encoded.png")
    encoded_image = XImage(fname="encoded.png").pixels
    
    print(f"The generated bitmap is {len(bitmask)} bits / {len(bitmask)/8} bytes long")
    assert (encoded == encoded_image).all()
    
    decoded = XBinaryString(string_data=encoder.decode(encoded=encoded_image, length=len(bitmask)))
    decoded_str = decoded.bytes_to_encoding()