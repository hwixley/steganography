from PIL import Image
import numpy as np
from services.steganographer import Steganographer
from base64 import b64decode, b64encode
from var.const import Default
from models.XMode import XMode
from models.XOutput import XOutput
from os.path import isfile


def save(arr: np.ndarray, fname: str):
    Image.fromarray(arr).save(fname)


if __name__ == "__main__":
    args = Default.arg_parser().parse_args()
    st = Steganographer()

    if args.mode == XMode.ENCODE:
        text = args.text
        if fpath := args.file:
            try:
                with open(fpath, "r") as f:
                    text = f.read()
            except Exception:
                print(f"[ ERROR ] The file '{fpath}' could not be opened, exiting...")
                exit(1)

        encoded, key = st.encode_text_to_image(
            text=text,
            image_path=args.input_image
        )
        save(arr=encoded, fname=args.export_path)
        print(f"[ SUCCESS ] Encoded image saved to '{args.export_path}'")

        if args.output_type == XOutput.INLINE:
            print(f"[ INFO ] Decoding Key: (! keep this safe, you need it for decoding !)")
            print(key)

            decoded = st.decode_text_from_image(
                image_path=args.export_path,
                key=key
            )
            print(f"[ INFO ] Decoded text from the generated '{args.export_path}' file:\n\"\"\"\n{decoded}\n\"\"\"")

        elif args.output_type == XOutput.FILE:
            fpath = f"{args.export_path}.key"
            print(f"[ INFO ] Exporting decoding key to '{fpath}' (! keep this safe, you need it for decoding !)")
            with open(fpath, "w") as f:
                f.write(key)
    
    elif args.mode == XMode.DECODE:
        kfile = f"{args.input_image}.key"
        key = args.key
        if key is None and isfile(kfile):
            try:
                with open(kfile, "r") as f:
                    key = f.read()
            except Exception:
                print(f"[ ERROR ] You have not specified a key, exiting...")
                exit(1)
        
        if key := key:
            print(key)
            decoded = st.decode_text_from_image(
                image_path=args.input_image,
                key=key
            )
            print(f"[ SUCCESS ] Decoded text from the encoded '{args.export_path}' file:\n\"\"\"\n{decoded}\n\"\"\"")
        else:
            print(f"[ ERROR ] You have not specified a key, exiting...")
            exit(1)

    else:
        print(f"[ ERROR ] invalid mode '{args.mode}', exiting...")
        exit(1)