import matplotlib.pyplot as plt
from argparse import ArgumentParser
from XImage import XImage
from pathlib import Path    

arg_parser = ArgumentParser()
arg_parser.add_argument(
    "--raw",
    "-r",
    type=Path,
    default="../sample.png"
)
arg_parser.add_argument(
    "--encoded",
    "-e",
    type=Path,
    default="../encoded.png"
)
args = arg_parser.parse_args()

raw = XImage(args.raw).pixels
encoded = XImage(args.encoded).pixels

if raw.shape != encoded.shape:
    print(f"Shapes do not match: raw {raw.shape}, encoded {encoded.shape}, exiting...")

diff = encoded - raw

plt.imshow(diff)
plt.show()