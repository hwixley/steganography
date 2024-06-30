from PIL import Image
import numpy as np
from services.steganographer import Steganographer
from argparse import ArgumentParser
from pathlib import Path


def save(arr: np.ndarray, fname: str):
    Image.fromarray(arr).save(fname)


default_text = "If you're reading this it means you did not input any custom text, or maybe you wanted to see this message instead, well if so it worked! WOOP Your image is now secretly encoded with this message."
default_img = "sample.png"
default_dest = "encoded.png"

arg_parser = ArgumentParser()
arg_parser.add_argument("--text", "-t", type=str, default=default_text)
arg_parser.add_argument("--image", "-i", type=Path, default=default_img)
arg_parser.add_argument("--output-path", "-o", type=Path, default=default_dest)


if __name__ == "__main__":
    args = arg_parser.parse_args()

    st = Steganographer()

    encoded, bm_len, bm_offset = st.encode_text_to_image(
        text=args.text,
        image_path=args.image
    )
    save(arr=encoded, fname=args.output_path)
    print(f"bm len: {bm_len}")
    print(f"bm offset: {bm_offset}")

    decoded = st.decode_text_from_image(
        image_path=args.output_path,
        length=bm_len,
        offset=bm_offset
    )

    print(decoded)