from enum import Enum
from typing import List

class XMode(str, Enum):
    ENCODE = "encode"
    DECODE = "decode"