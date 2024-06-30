from PIL import Image
import numpy as np

class XImage:

    def __init__(self, fname: str):
        self.fname = fname
        self.pixels = self.load_image()

    def load_image(self) -> np.ndarray:
        try:
            img = Image.open(self.fname)
            return np.array(img)
        except FileNotFoundError as e:
            print(e)
            print("Exiting...")
            exit(1)




