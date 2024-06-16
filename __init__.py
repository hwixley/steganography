from models.Image import XImage
from models.Encoder import Encoder
import numpy as np

image = XImage(fname="sample.png")
encoder = Encoder(message="Hello good sir this is a dear message that I hope finds you well I hope the supplementary image was complementary tooProps on getting to this point it means the script must have worked")

if __name__ == "__main__":
    binary = encoder.binary_bool()
    encoded = image.bitmap_encode(bitmap=binary)
    image.save(arr=encoded, fname="encoded.png")
    print(f"The generated bitmap is {len(binary)} bits / {len(binary)/8} bytes long")

    decoded = image.bitmap_decode(encoded=encoded)
    # print(decoded[0]/)
    decoded_str = encoder.binary_to_str(decoded)
    print(decoded_str)
    # image.save(arr=decoded, fname="decoded.png")
    