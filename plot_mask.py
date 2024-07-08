import matplotlib.pyplot as plt
from argparse import ArgumentParser
from models.XImage import XImage
from pathlib import Path    
import numpy as np
from math import ceil

arg_parser = ArgumentParser()
arg_parser.add_argument(
    "--raw",
    "-r",
    type=Path,
    default="sample.png"
)
arg_parser.add_argument(
    "--encoded",
    "-e",
    type=Path,
    default="sample._encoded.png"
)
args = arg_parser.parse_args()

raw = XImage(args.raw).pixels
encoded = XImage(args.encoded).pixels

if raw.shape != encoded.shape:
    print(f"Shapes do not match: raw {raw.shape}, encoded {encoded.shape}, exiting...")

diff = encoded - raw

def plot_row(ax: plt.Axes, row_idx: int, img: np.ndarray, name: str):
    img = img*255/np.max(img)
    ax[row_idx,0].imshow(img)
    ax[row_idx,1].imshow(img[:,:,0])
    ax[row_idx,2].imshow(img[:,:,1])
    ax[row_idx,3].imshow(img[:,:,2])
    ax[row_idx,0].set_ylabel(name)

fig, axs = plt.subplots(3,4)

plot_row(axs, 0, raw, "Raw")
plot_row(axs, 1, encoded, "Encoded")
plot_row(axs, 2, diff, "Diff")

axs[2,0].set_xlabel("All Channels")
axs[2,1].set_xlabel("Channel 1")
axs[2,2].set_xlabel("Channel 2")
axs[2,3].set_xlabel("Channel 3")
plt.suptitle("Comparing Raw & Encoded Versions of the Same Images\nto Inspect The Quality of the Encoding")

# idx = 0
# llen, offset = 191, 149219
# coords = []
# min_i, min_j, min_k = 1e+20, 1e+20, 1e+20
# max_i, max_j, max_k = 0, 0, 0
# for i in range(encoded.shape[0]):
#     for j in range(encoded.shape[1]):
#         for k in range(encoded.shape[2]):
#             if idx >= offset and idx < offset + llen:
#                 axs[0,0].plot(i,j,color="red", marker='o', ms=1)
#                 coords.append((i,j,k))
#                 min_i, min_j, min_k = min(min_i, i), min(min_j, j), min(min_k, k)
#                 max_i, max_j, max_k = max(max_i, i), max(max_j, j), max(max_k, k)
#             elif idx >= offset + llen:
#                 break
#             idx += 1

# sslice = diff[min_i:max_i+1,min_j:max_j+1, :]
# print(sslice.shape)
# nlen = ceil(np.sqrt(np.prod(sslice.shape[0:2])))
# sslice = sslice.reshape(nlen, nlen)
# print(sslice.shape)
# axs[3,0].imshow(sslice)
plt.show()