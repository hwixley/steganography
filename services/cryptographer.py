from base64 import b64encode, b64decode
from typing import Tuple

class Cryptographer:

    @staticmethod
    def obf_key(text: str) -> str:
        return b64encode(text.encode()).decode()
    
    @staticmethod
    def deobf_key(obf_text: str) -> Tuple[int, int]:
        try:
            deobf = b64decode(obf_text.encode()).decode()
            vals = deobf.split("-")
            return int(vals[0]), int(vals[1])
        except Exception:
            print("ERROR: the key you have entered is invalid, exiting...")
            exit(1)