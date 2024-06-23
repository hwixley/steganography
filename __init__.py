from PIL import Image
import numpy as np
from services.steganographer import Steganographer

def save(arr: np.ndarray, fname: str):
    Image.fromarray(arr).save(fname)


test_text="Hello good sir this is a dear message that I hope finds you well I hope the supplementary image was complementary tooProps on getting to this point it means the script must have worked"

if __name__ == "__main__":
    st = Steganographer()

    encoded, bm_len = st.encode_text_to_image(
        text=test_text,
        image_path="sample.png"
    )
    save(arr=encoded, fname="encoded.png")

    decoded = st.decode_text_from_image(
        image_path="encoded.png",
        length=bm_len
    )

    print(decoded)