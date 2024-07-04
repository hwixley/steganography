from PIL import Image
import numpy as np
from services.steganographer import Steganographer
from argparse import ArgumentParser
from pathlib import Path
from models.XMode import XMode
from base64 import b64decode, b64encode


def save(arr: np.ndarray, fname: str):
    Image.fromarray(arr).save(fname)


default_mode = XMode.ENCODE
default_text = "If you're reading this it means you did not input any custom text, or maybe you wanted to see this message instead, well if so it worked! WOOP Your image is now secretly encoded with this message."
default_img = "sample.png"
default_dest = "encoded.png"

arg_parser = ArgumentParser()
arg_parser.add_argument("--mode", "-m", type=XMode, default=default_mode)
arg_parser.add_argument("--text", "-t", type=str, default=default_text)
arg_parser.add_argument("--file", "-f", type=Path)
arg_parser.add_argument("--image", "-i", type=Path, default=default_img)
arg_parser.add_argument("--output-path", "-o", type=Path, default=default_dest)
arg_parser.add_argument("--key", "-k", type=str)

if __name__ == "__main__":
    args = arg_parser.parse_args()

    st = Steganographer()

    if args.mode == XMode.ENCODE:
        data = args.file or args.text

        encoded, key = st.encode_text_to_image(
            text=data,
            image_path=args.image
        )
        save(arr=encoded, fname=args.output_path)
        print(f"Decoding Key: (! keep this safe, you need it for decoding !)")
        print(key)

        decoded = st.decode_text_from_image(
            image_path=args.output_path,
            key=key
        )

        print(f"\nDecoded text from the generated '{args.output_path}' file:\n\"\"\"\n{decoded}\n\"\"\"")
    
    elif args.mode == XMode.DECODE:
        if key := args.key:
            decoded = st.decode_text_from_image(
                image_path=args.image,
                key=key
            )

            print(f"\nDecoded text from the encoded '{args.output_path}' file:\n\"\"\"\n{decoded}\n\"\"\"")
        else:
            print(f"ERROR: you have not specified a key, exiting...")
            exit(1)

    else:
        print(f"ERROR: invalid mode '{args.mode}', exiting...")
        exit(1)