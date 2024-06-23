from models.Image import XImage
from models.Text import Text
from models.Binary import BinaryBytes, BinaryString

image = XImage(fname="sample.png")
text = Text(text="Hello good sir this is a dear message that I hope finds you well I hope the supplementary image was complementary tooProps on getting to this point it means the script must have worked")


if __name__ == "__main__":
    binary = BinaryBytes(bytes_data=text.to_bytes())
    bits = binary.to_bits_array()
    encoded = image.bitmap_encode(bits=bits)
    image.save(arr=encoded, fname="encoded.png")
    print(f"The generated bitmap is {len(bits)} bits / {len(bits)/8} bytes long")

    encoded_image = XImage(fname="encoded.png").pixels
    assert (encoded == encoded_image).all()
    decoded = BinaryString(string_data=image.bitmap_decode(encoded=encoded_image, length=len(bits)))
    decoded_str = decoded.bytes_to_encoding()
    # print(decoded_str)
    # image.save(arr=decoded, fname="decoded.png")
    