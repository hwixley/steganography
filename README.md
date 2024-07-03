# 🔏 Steganography - hiding secret data in media files
This repository enables the (en|de)coding of secret data in media files.

## Supported Media Types
1. Image - PPM, PNG, JPEG, GIF, TIFF, and BMP

## Installation
1. Clone the repo:
```
git clone git@github.com:hwixley/steganography.git
```
2. Run the script:
```
python3 __init__.py <args>
```

## Arguments
- `--mode <encode|decode>` | `-m <encode|decode>` - the mode you want to run.
    - Encoding mode args:
        - `--text <text>` | `-t <text>` - the text you want to encode.
        - `--image <image-path>` | `-i <image-path>` - the image you want to encode the text onto.
        - `--output_path <output-path>` | `-o <output-path>` - the output path for your encoded image.
    - Decoding mode args:
        - `--image <image-path>` | `-i <image_path>` - the image you want to decode text from.
        - `--key <key>` | `-k <key>` - the key to enable the decoding of the image.

